#!/bin/bash
# mix.sh VOIX MUSIQUE VIDEO SORTIE "t1 t2 ..." (moments des whoosh)
V=$1; M=$2; VID=$3; OUT=$4; WT=$5
DUR=$(ffprobe -v error -show_entries format=duration -of csv=p=0 $VID)
# 1) voix : nettoyage + présence + compression + -14 LUFS
ffmpeg -loglevel error -y -i $V -af "highpass=f=85,lowpass=f=15000,agate=threshold=0.015:ratio=2.5:attack=3:release=150,equalizer=f=220:t=q:w=1:g=-2.5,equalizer=f=3200:t=q:w=1.2:g=3,deesser=i=0.4,acompressor=threshold=-20dB:ratio=3.5:attack=4:release=90:makeup=3,loudnorm=I=-14:TP=-1.5:LRA=6" -ar 48000 -ac 2 voix_ok.wav
# 2) whoosh + boom
INS="-i boom.wav"; FC="[1:a]adelay=0|0,volume=0.55[b0];"; MIXL="[b0]"; k=2
for t in $WT; do ms=$(python3 -c "print(int($t*1000)-200)"); INS="$INS -i whoosh.wav"; FC="$FC[$k:a]adelay=$ms|$ms,volume=0.22[w$k];"; MIXL="$MIXL[w$k]"; k=$((k+1)); done
n=$((k-1))
ffmpeg -loglevel error -y -f lavfi -i "anullsrc=r=48000:cl=stereo:d=$DUR" $INS -filter_complex "${FC}[0:a]${MIXL}amix=inputs=$((n+1)):normalize=0:duration=first[s]" -map "[s]" sfx.wav
# 3) musique en boucle, ducking sous la voix (sidechain)
ffmpeg -loglevel error -y -stream_loop -1 -i $M -i voix_ok.wav -i sfx.wav -filter_complex "\
[0:a]atrim=0:$DUR,asetpts=N/SR/TB,highpass=f=35,volume=0.30,afade=t=in:d=0.4,afade=t=out:st=$(python3 -c "print($DUR-1.2)"):d=1.2,aresample=48000[m];\
[1:a]apad=whole_dur=$DUR,asplit=2[v][key];\
[m][key]sidechaincompress=threshold=0.02:ratio=5:attack=15:release=350:makeup=1[md];\
[v][md][2:a]amix=inputs=3:normalize=0:duration=first,alimiter=limit=0.93[a]" -map "[a]" -ar 48000 mix.wav
ffmpeg -loglevel error -y -i $VID -i mix.wav -map 0:v -map 1:a -c:v libx264 -preset slow -b:v 9M -maxrate 12M -bufsize 16M -pix_fmt yuv420p -c:a aac -b:a 256k -movflags +faststart -shortest $OUT
ffmpeg -i $OUT -af ebur128 -f null - 2>&1 | grep -E "^\s+I:" | tail -1
