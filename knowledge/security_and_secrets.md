*TAGS: build, business-plan | AUDIENCE: founder + every future Claude (READ before writing back-end code, wiring any API, or handling customer data).*
*CREATED: 2026-06-08, Chat 6 | UPDATED: 2026-06-10, Chat 7 (added the FABLE 5 RETENTION CONSTRAINT + a MODEL-DATA-RETENTION launch gate — Fable 5/Mythos 5 = Covered Models, mandatory 30-day retention, NO ZDR on the Claude API; verified Chat 7 vs official docs; Opus 4.8 stays ZDR-eligible. Companion to the model-tiering decision in tech_architecture_skeleton.md) | STATUS: captured (launch gates OPEN until done)*
*SUPERSEDES: — | RELATED: tech_architecture_skeleton.md (the 7-tool stack), repo_as_memory_and_handoff.md (the repo is PUBLIC), credit_value_pricing_model.md (Stripe/keys)*

# GOLD — SECURITY & SECRETS (the back end must be secure)

## ONE-LINE
Every API key is a loaded weapon and the public repo + the customer DB are the prizes. Build these rules
in from day one (cheap) — never retrofit after a breach (expensive). When in doubt, say less / store less.

## THE TRADEIFY LESSON (why this doc exists — June 2026)
Tradeify (a top-3 prop firm) was breached and 100,000+ traders got flooded with phishing emails. The hole
was **NOT** their core trading system — it was a **third-party email-marketing tool**, entered via a
**compromised API key**, which exposed their **customer database (names + emails)**. What saved them:
passwords, KYC, payment info, and balances lived in *separate* systems and were not touched. **Takeaway: a
single leaked API key to a connected vendor became the skeleton key to every customer record.** bioniq has
the same shape of risk — many third-party keys (Anthropic, ElevenLabs, datafeed, Stripe, email) and a
customer DB in Supabase (names, emails, dossier, ledger). This is our threat model, handed to us for free.

## STANDING RULES (non-negotiable)
1. **API keys are loaded weapons.** Never in client-side code, never in the repo, never in a screenshot or
   chat. Server-side environment variables / a secrets manager ONLY. Scope each key to the minimum it needs;
   rotate on a schedule and immediately on any suspicion.
2. **THE REPO IS PUBLIC — zero secrets, zero customer data, ever.** A key committed to a public GitHub repo
   is found by bots in minutes. The goldmine holds *strategy and decisions* — never credentials, `.env`
   files, tokens, or PII. (A secrets-scan is part of KICKOFF_AUDIT.)
3. **Supabase holds the "names + emails" prize — lock the access model.** Row-Level Security (RLS) on every
   table so a leaked anon key (or one user) can never dump the whole table. Misconfigured RLS is the most
   common Supabase breach. **RLS review is a launch gate.**
4. **Use the edge you already pay for.** Cloudflare = WAF + rate-limiting + (via AI Gateway) spend-caps and
   the single choke point in front of Claude. It limits blast radius — configure it, don't just host on it.
5. **Minimize what you collect / hand to vendors.** Tradeify's prize was names+emails because that's what
   the marketing tool held. Keep sensitive data in OUR controlled store (the dossier-is-the-moat instinct),
   not scattered across third-party tools. Less PII out = smaller prize.
6. **Phishing is the downstream damage — set sender auth early.** SPF/DKIM/DMARC on the bioniq domain and
   "we only email from @bioniq..." messaging, so spoofed "bioniq" emails are harder and users know the real
   sender. (Tradeify's traders got phished *because* the attacker had their emails.)

## LAUNCH GATES (must clear BEFORE real customer data or money)
- [ ] Secrets audit — no keys in repo/client; all server-side + scoped + rotated.
- [ ] Supabase RLS review — every table, deny-by-default.
- [ ] Cloudflare WAF + rate-limits + AI-Gateway spend caps configured.
- [ ] SPF/DKIM/DMARC set on the domain.
- [ ] **Independent security pass** — secrets scan + RLS review + a pen-test or OWASP-Top-10 checklist.
- [ ] **MODEL-DATA-RETENTION gate (Chat 7) — Fable 5 vs sensitive dossiers.** Mark **DECISION required**
      before any real customer dossier (PII / full trade history) is routed through **Claude Fable 5**.
      *Verification CLOSED, decision OPEN.*

## FABLE 5 RETENTION CONSTRAINT (VERIFIED Chat 7 — the model-tiering security tension)
The model-tiering decision lives in `tech_architecture_skeleton.md` (Opus 4.8 workhorse / Fable 5 metered
premium). Its **security half** lands here. Mark flagged the retention terms as *reported, not yet verified*;
the PHD ran the verification he named and it came back **CONFIRMED** against official Anthropic docs:
- **Claude Fable 5 (and Mythos 5) are "Covered Models" requiring 30-day data retention.** **Zero Data
  Retention is NOT available** for them on the Claude API — a ZDR-configured org gets a
  `400 invalid_request_error`. Data is **not used for training** and is **deleted after 30 days** (except a
  safety investigation or legal hold). On Bedrock / Vertex / Foundry, retention is set per platform (Bedrock
  requires opting into provider data sharing).
- **Opus 4.8 remains ZDR-eligible** — the ZDR-safe default for anything sensitive.
- **THE TENSION:** routing our **most sensitive deep-dossier reviews** through Fable would put them on the
  model with the **least favourable retention terms** — directly counter to "minimize PII to vendors."
- **POSTURE until Mark decides:** **Fable is NOT cleared for sensitive customer data.** Premium Fable
  deep-reviews run only on **de-identified / non-PII** inputs, OR the dossier is routed to **Opus**, OR Mark
  accepts the 30-day window for specific data classes that tolerate it. Build the route so the **default is
  Opus** and Fable requires an explicit, logged premium flag (structural, not a reminder).
- **Sources (official):** platform.claude.com → Manage Claude → "API and data retention"; support.claude.com
  → "Data retention practices for Mythos-class models" (art. 15425996).

## THE HONEST LIMIT
Claude is a solid first-principles guide for threat model + architecture + the checklist — but security is
the ONE area where "pretty good from an AI" is not enough before holding real customer data and money. Get
a proper independent review before launch. Claude helps build the checklist; Claude is NOT the sole sign-off.

## INDEX LINE
`knowledge/security_and_secrets.md | build, business-plan | PUBLIC | captured | SECURITY & SECRETS — the back end must be secure. Tradeify lesson (June 2026): a leaked API key to a 3rd-party email tool exposed 100k+ customers (names+emails); core systems were safe because they were separate. Our same-shape risk: many vendor keys + a Supabase customer DB. RULES: API keys are loaded weapons (server-side only, scoped, rotated, NEVER in the PUBLIC repo or client); repo holds strategy not secrets/PII; Supabase RLS on every table (deny-by-default); use Cloudflare WAF/rate-limit/spend-caps; minimize PII handed to vendors; SPF/DKIM/DMARC for anti-phishing. LAUNCH GATES before real data/money: secrets audit, RLS review, CF config, email auth, INDEPENDENT security pass, + (Chat 7) MODEL-DATA-RETENTION gate — Fable 5/Mythos 5 are Covered Models w/ mandatory 30-day retention + NO ZDR on the Claude API (verified Chat 7); Opus 4.8 stays ZDR-eligible; Fable NOT cleared for sensitive customer dossiers until Mark decides (companion to model-tiering in tech_architecture_skeleton.md). Claude guides, is NOT the sole security sign-off.`
