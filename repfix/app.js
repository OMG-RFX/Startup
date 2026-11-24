/* RepFix : suivi sans cookie + liste d'attente. La provenance (UTM + référent) est gardée
   dans le stockage de session de l'onglet, effacé à sa fermeture. */
(function () {
  "use strict";
  var SITE_URL = "https://omg-rfx.github.io/Startup/repfix";
  // Adresse de réception des inscriptions (Web3Forms). La clé d'accès est publique par conception : elle ne permet que d'envoyer vers notre boîte mail.
  var FORM_ENDPOINT = "https://api.web3forms.com/submit";
  var FORM_KEY = "7e5a2111-1f66-48e5-9163-1991cba90904";
  var CAMPAIGN = "test_coach";
  var PAGE = /[?&]__test=1\b/.test(location.search) ? "test" : "coach";
  var UTM = ["utm_source", "utm_medium", "utm_campaign", "utm_content", "utm_term"];
  var KEY = "reps_attr";
  var attr = null;
  var reduce = window.matchMedia && matchMedia("(prefers-reduced-motion: reduce)").matches;

  /* --- Compteur partagé avec le tableau de bord Oh My Glow (gratuit, sans cookie) --- */
  var COUNTER = "https://abacus.jasoncameron.dev/hit/ohmyglow-x7k2q9/";
  var SOURCES = ["tiktok", "instagram", "youtube_shorts", "snapchat", "tiktok_us", "instagram_us", "youtube_shorts_us", "snapchat_us", "meta_ads", "bouche_a_oreille", "partage", "direct"];
  var COUNTER_EVENTS = { visit: "visite", scroll_50: "scroll-50", cta_click: "clic-formulaire", share_click: "partage", signup: "inscription" };
  function counterSource() {
    var s = (getAttr().utm_source || "").toLowerCase();
    if (s) return SOURCES.indexOf(s) >= 0 ? s : "autre";
    var r = (document.referrer || "").toLowerCase();
    if (!r || r.indexOf(location.origin) === 0) return "direct";
    if (/tiktok/.test(r)) return "tiktok";
    if (/instagram/.test(r)) return "instagram";
    if (/youtube|youtu\.be/.test(r)) return "youtube_shorts";
    if (/snapchat/.test(r)) return "snapchat";
    if (/facebook|fb\./.test(r)) return "meta_ads";
    return "autre";
  }
  function counterHit(key) { try { fetch(COUNTER + key, { mode: "cors", keepalive: true }).catch(function () {}); } catch (e) {} }
  function counterOnce(flag) {
    try { if (sessionStorage.getItem(flag)) return false; sessionStorage.setItem(flag, "1"); } catch (e) {}
    return true;
  }
  function counterTrack(event) {
    var name = COUNTER_EVENTS[event];
    if (!name || PAGE !== "coach") return;
    if (event !== "signup" && event !== "share_click" && !counterOnce("reps_cnt_" + name)) return;
    var src = counterSource();
    counterHit("coach." + name + ".total");
    counterHit("coach." + name + "." + src);
    if (event === "visit") {
      var d = new Date();
      counterHit("coach.visite.d" + d.getFullYear() + "-" + String(d.getMonth() + 1).padStart(2, "0") + "-" + String(d.getDate()).padStart(2, "0"));
    }
  }
  /* --- fin du compteur --- */

  function getAttr() {
    if (attr) return attr;
    var params = new URLSearchParams(location.search);
    var stored = null;
    try { stored = JSON.parse(sessionStorage.getItem(KEY) || "null"); } catch (e) {}
    var urlHasUtm = UTM.some(function (k) { return params.get(k); });
    if (!urlHasUtm && stored) return (attr = stored);
    var ext = document.referrer && document.referrer.indexOf(location.origin) !== 0 ? document.referrer : "";
    var a = {};
    UTM.forEach(function (k) { a[k] = (params.get(k) || "").slice(0, 100); });
    a.referrer = (ext || (stored && stored.referrer) || "").slice(0, 300);
    a.landing = (location.pathname + location.search).slice(0, 300);
    try { sessionStorage.setItem(KEY, JSON.stringify(a)); } catch (e) {}
    return (attr = a);
  }

  var PLAUSIBLE = { cta_click: "Clic inscription", scroll_50: "Defilement 50", share_click: "Partage", signup: "Inscription" };
  function track(event, label) {
    var a = getAttr();
    counterTrack(event);
    if (typeof window.plausible === "function" && PLAUSIBLE[event]) {
      try { window.plausible(PLAUSIBLE[event], { props: { detail: label || "", source: a.utm_source || "(aucune)" } }); } catch (e) {}
    }
    // Les inscriptions sont envoyées par email via Web3Forms (FORM_ENDPOINT) ; le compteur s'occupe des statistiques.
  }

  // Visite + défilement à 50 %
  track("visit");
  var scrolled = false;
  function onScroll() {
    if (scrolled) return;
    var h = document.documentElement.scrollHeight;
    if (h > 0 && (scrollY + innerHeight) / h >= 0.5) {
      scrolled = true;
      track("scroll_50");
      removeEventListener("scroll", onScroll);
    }
  }
  addEventListener("scroll", onScroll, { passive: true });

  // Boutons qui mènent au formulaire
  function goToForm(label) {
    track("cta_click", label);
    var el = document.getElementById("rejoindre");
    if (!el) return;
    el.scrollIntoView({ behavior: reduce ? "auto" : "smooth", block: "start" });
    setTimeout(function () {
      var i = el.querySelector("input[type=email]");
      if (i) i.focus({ preventScroll: true });
    }, reduce ? 0 : 550);
  }
  document.querySelectorAll("[data-cta]").forEach(function (b) {
    b.addEventListener("click", function () { goToForm(b.getAttribute("data-cta")); });
  });

  // Formulaires (deux copies du même modèle)
  var done = null;
  var EMAIL_RE = /^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/;
  var slots = document.querySelectorAll("[data-form]");
  var uid = 0;
  slots.forEach(function (slot) { mountForm(slot, slot.getAttribute("data-form")); });

  function mountForm(slot, loc) {
    var frag = document.getElementById("tpl-form").content.cloneNode(true);
    var p = "f" + ++uid + "-";
    frag.querySelectorAll("[data-id]").forEach(function (el) { el.id = p + el.getAttribute("data-id"); });
    frag.querySelectorAll("[data-for]").forEach(function (el) { el.setAttribute("for", p + el.getAttribute("data-for")); });
    frag.querySelectorAll("[data-err]").forEach(function (el) { el.id = p + el.getAttribute("data-err") + "-err"; });
    slot.innerHTML = "";
    slot.appendChild(frag);
    var form = slot.querySelector("form");
    var q = function (n) { return document.getElementById(p + n); };
    var status = form.querySelector(".form-status");
    var btn = form.querySelector(".btn-submit");
    var btnLabel = btn.querySelector("span");

    function setErr(name, msg) {
      var input = q(name), err = q(name + "-err");
      if (!err) return;
      if (msg) {
        err.textContent = msg; err.hidden = false;
        input.setAttribute("aria-invalid", "true"); input.setAttribute("aria-describedby", err.id);
      } else {
        err.hidden = true; input.removeAttribute("aria-invalid"); input.removeAttribute("aria-describedby");
      }
    }

    form.addEventListener("submit", function (e) {
      e.preventDefault();
      track("cta_click", "envoi_" + loc);
      var email = q("email").value.trim(), fn = q("fn").value.trim();
      var errs = {
        email: EMAIL_RE.test(email) ? "" : "Entre une adresse email valide.",
        consent: q("consent").checked ? "" : "Coche cette case pour qu'on puisse te prévenir du lancement.",
        age: q("age").checked ? "" : "L'inscription est réservée aux 15 ans et plus.",
      };
      var first = null;
      Object.keys(errs).forEach(function (k) { setErr(k, errs[k]); if (errs[k] && !first) first = k; });
      if (first) { q(first).focus(); return; }
      btn.disabled = true; btnLabel.textContent = "Inscription en cours…"; status.textContent = "";
      var at = getAttr();
      var data = {
        access_key: FORM_KEY, subject: "Inscription RepFix", from_name: "RepFix", botcheck: q("web").value ? true : false,
        email: email, prenom: fn, optin: "oui", age: "oui",
        page: PAGE, emplacement: loc, utm_source: at.utm_source || "", utm_medium: at.utm_medium || "",
        utm_campaign: at.utm_campaign || "", utm_content: at.utm_content || "", referent: at.referrer || "",
        date: new Date().toISOString()
      };
      fetch(FORM_ENDPOINT, {
        method: "POST",
        headers: { "Accept": "application/json", "Content-Type": "application/json" },
        body: JSON.stringify(data),
      }).then(function (r) {
        return r.json().catch(function () { return {}; }).then(function (j) {
          var good = r.ok && String(j.success) === "true";
          return { ok: good, d: { ok: good } };
        });
      }).then(function (res) {
        if (!res.ok || !res.d.ok) {
          status.textContent = res.d.error === "email" ? "Cette adresse email ne semble pas valide."
            : res.d.error === "trop_de_tentatives" ? "Trop de tentatives. Réessaie dans quelques minutes."
            : "Oups, l'inscription n'est pas passée. Réessaie dans un instant.";
          btn.disabled = false; btnLabel.textContent = "Rejoindre la liste d'attente";
          return;
        }
        if (!res.d.already) track("signup", loc);
        done = { firstName: fn, already: !!res.d.already };
        slots.forEach(function (s) { showThanks(s); });
        var t = slot.querySelector(".thanks"); if (t) t.focus();
        updateSticky();
      }).catch(function () {
        status.textContent = "Pas de connexion ? L'inscription n'est pas passée, réessaie dans un instant.";
        btn.disabled = false; btnLabel.textContent = "Rejoindre la liste d'attente";
      });
    });
  }

  function showThanks(slot) {
    var frag = document.getElementById("tpl-thanks").content.cloneNode(true);
    frag.querySelector(".thanks-title").textContent =
      (done.already ? "Tu es déjà sur la liste" : "Bienvenue sur la liste") + (done.firstName ? ", " + done.firstName : "") + " !";
    var b = frag.querySelector(".btn-share"), lab = b.querySelector("span");
    b.addEventListener("click", function () {
      track("share_click", "merci");
      var url = SITE_URL + "/?utm_source=bouche_a_oreille&utm_medium=partage&utm_campaign=" + CAMPAIGN;
      var text = "Je viens de rejoindre la liste d'attente de RepFix : une appli qui corrige ta technique à la salle et adapte ton programme. Inscris-toi aussi :";
      var copy = function () {
        if (navigator.clipboard) {
          navigator.clipboard.writeText(text + " " + url).then(function () {
            lab.textContent = "Lien copié, envoie-le !";
            setTimeout(function () { lab.textContent = "Partager à un pote de salle"; }, 3000);
          }, function () { prompt("Copie ce lien et envoie-le à ton pote :", url); });
        } else prompt("Copie ce lien et envoie-le à ton pote :", url);
      };
      if (navigator.share) {
        navigator.share({ title: "RepFix, ton coach de salle dans la poche", text: text, url: url })
          .catch(function (err) { if (!err || err.name !== "AbortError") copy(); });
      } else copy();
    });
    slot.innerHTML = "";
    slot.appendChild(frag);
  }

  // Bouton collant (mobile) : visible quand ni le bouton du haut ni un formulaire ne sont à l'écran
  var sticky = document.getElementById("sticky-cta");
  var stickyBtn = sticky.querySelector("button");
  var visible = new Set();
  function updateSticky() {
    var on = !done && visible.size === 0 && scrollY > 200;
    sticky.classList.toggle("is-on", on);
    sticky.setAttribute("aria-hidden", on ? "false" : "true");
    stickyBtn.tabIndex = on ? 0 : -1;
  }
  if ("IntersectionObserver" in window) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) { en.isIntersecting ? visible.add(en.target) : visible.delete(en.target); });
      updateSticky();
    });
    [document.getElementById("hero-cta")].concat([].slice.call(document.querySelectorAll("[data-formzone]")))
      .forEach(function (t) { if (t) io.observe(t); });
  }
})();
