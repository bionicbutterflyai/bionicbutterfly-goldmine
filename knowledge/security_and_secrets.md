*TAGS: build, business-plan | AUDIENCE: founder + every future Claude (READ before writing back-end code, wiring any API, or handling customer data).*
*CREATED: 2026-06-08, Chat 6 | UPDATED: 2026-06-08, Chat 6 | STATUS: captured (launch gates OPEN until done)*
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

## THE HONEST LIMIT
Claude is a solid first-principles guide for threat model + architecture + the checklist — but security is
the ONE area where "pretty good from an AI" is not enough before holding real customer data and money. Get
a proper independent review before launch. Claude helps build the checklist; Claude is NOT the sole sign-off.

## INDEX LINE
`knowledge/security_and_secrets.md | build, business-plan | PUBLIC | captured | SECURITY & SECRETS — the back end must be secure. Tradeify lesson (June 2026): a leaked API key to a 3rd-party email tool exposed 100k+ customers (names+emails); core systems were safe because they were separate. Our same-shape risk: many vendor keys + a Supabase customer DB. RULES: API keys are loaded weapons (server-side only, scoped, rotated, NEVER in the PUBLIC repo or client); repo holds strategy not secrets/PII; Supabase RLS on every table (deny-by-default); use Cloudflare WAF/rate-limit/spend-caps; minimize PII handed to vendors; SPF/DKIM/DMARC for anti-phishing. LAUNCH GATES before real data/money: secrets audit, RLS review, CF config, email auth, INDEPENDENT security pass. Claude guides, is NOT the sole security sign-off.`
