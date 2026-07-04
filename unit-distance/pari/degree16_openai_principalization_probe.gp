\\ Degree-16 PARI/GP probe for the OpenAI unit-distance construction.
\\
\\ This deliberately avoids Sage's relative-field ideal arithmetic.  It works
\\ in the absolute field K = Q(i, sqrt(5), sqrt(13), sqrt(17)), detects the CM
\\ conjugation automorphism, pairs split prime ideals over p, then searches for
\\ principal collisions among the OpenAI-style ideals
\\
\\     J(a) = prod_h P_h^a_h * c(P_h)^(k-a_h).
\\
\\ Usage:
\\   /Users/gpeyre/miniconda3/envs/unit-distance-sage/bin/gp -q \
\\     unit-distance/pari/degree16_openai_principalization_probe.gp

p = 101;
k = 2;
pair_limit = 8;
max_report = 6;

canonical_mod_vector(v, cyc) =
{
  vector(length(cyc), r, lift(Mod(v[r], cyc[r])));
};

zero_class(cyc) =
{
  vector(length(cyc), r, 0);
};

class_add_scaled(acc, v, scale, cyc) =
{
  my(out = vector(length(cyc), r, acc[r]));
  for (r = 1, length(cyc),
    out[r] = lift(Mod(out[r] + scale * v[r], cyc[r]));
  );
  out;
};

build_compositum_pol() =
{
  my(x = 'x, pol);
  pol = polcompositum(x^2 + 1, x^2 - 5)[1];
  pol = polcompositum(pol, x^2 - 13)[1];
  pol = polcompositum(pol, x^2 - 17)[1];
  pol;
};

detect_cm_conjugation(nf, pol, auts) =
{
  my(x = 'x, z, best, cm_index, d);
  z = nfeltembed(nf, Mod(x, pol))[1];
  best = 10^100;
  cm_index = 0;
  for (h = 1, length(auts),
    d = abs(nfeltembed(nf, auts[h])[1] - conj(z));
    if (d < best,
      best = d;
      cm_index = h;
    );
  );
  [cm_index, best];
};

pair_prime_ideals(nf, dec, cm) =
{
  my(n = length(dec), used, pairs, target, match);
  used = vector(n, h, 0);
  pairs = List();
  for (h = 1, n,
    if (!used[h],
      target = idealhnf(nf, nfgaloisapply(nf, cm, dec[h]));
      match = 0;
      for (j = 1, n,
        if (!used[j] && idealhnf(nf, dec[j]) == target,
          match = j;
          break();
        );
      );
      if (match == 0,
        error("Could not pair prime ideal under CM conjugation.");
      );
      used[h] = 1;
      used[match] = 1;
      listput(pairs, [h, match]);
    );
  );
  Vec(pairs);
};

decode_exponents(record_id, base, m) =
{
  my(q = record_id, a, exps);
  exps = vector(m, h, 0);
  for (h = 1, m,
    a = q - base * floor(q / base);
    q = floor(q / base);
    exps[h] = a;
  );
  exps;
};

class_of_exponents(exps, eP, ePc, k, cyc) =
{
  my(e = zero_class(cyc), a);
  for (h = 1, length(exps),
    a = exps[h];
    e = class_add_scaled(e, eP[h], a, cyc);
    e = class_add_scaled(e, ePc[h], k - a, cyc);
  );
  e;
};

build_J(nf, dec, pairs, exps, k) =
{
  my(J, P, Pc, a);
  J = idealhnf(nf, 1);
  for (h = 1, length(exps),
    a = exps[h];
    P = idealhnf(nf, dec[pairs[h][1]]);
    Pc = idealhnf(nf, dec[pairs[h][2]]);
    if (a > 0,
      J = idealmul(nf, J, idealpow(nf, P, a));
    );
    if (k - a > 0,
      J = idealmul(nf, J, idealpow(nf, Pc, k - a));
    );
  );
  J;
};

main() =
{
  my(
    pol, nf, auts, cm_data, cm_index, cm_error, cm,
    dec, pairs_all, pair_count, pairs, bnf, cyc, eP, ePc,
    base, record_count, exponents, classes, reported, done,
    delta, JL, JR, ratio, principal, gam, gam_c, gam_emb, gam_c_emb, u_emb
  );

  print("degree16_openai_principalization_probe");
  print("p=", p, " k=", k, " pair_limit=", pair_limit);

  gettime();
  pol = build_compositum_pol();
  print("polynomial_degree=", poldegree(pol));
  print("field_polynomial=", pol);
  print("field_build_ms=", gettime());

  gettime();
  nf = nfinit(pol);
  auts = nfgaloisconj(nf);
  cm_data = detect_cm_conjugation(nf, pol, auts);
  cm_index = cm_data[1];
  cm_error = cm_data[2];
  cm = auts[cm_index];
  print("automorphisms=", length(auts));
  print("cm_index=", cm_index);
  print("cm_detection_error=", cm_error);
  print("nf_and_aut_ms=", gettime());

  gettime();
  dec = idealprimedec(nf, p);
  pairs_all = pair_prime_ideals(nf, dec, cm);
  pair_count = min(pair_limit, length(pairs_all));
  pairs = vector(pair_count, h, pairs_all[h]);
  print("split_prime_ideals=", length(dec));
  print("cm_pairs_total=", length(pairs_all));
  print("cm_pairs_used=", pair_count);
  for (h = 1, pair_count,
    print("pair_", h, "=", pairs[h]);
  );
  print("prime_pairing_ms=", gettime());

  gettime();
  bnf = bnfinit(pol, 1);
  cyc = bnf.cyc;
  print("class_number=", bnf.no);
  print("class_group_cyc=", cyc);
  print("bnf_ms=", gettime());

  gettime();
  eP = vector(pair_count);
  ePc = vector(pair_count);
  for (h = 1, pair_count,
    eP[h] = canonical_mod_vector(bnfisprincipal(bnf, idealhnf(nf, dec[pairs[h][1]]), 0), cyc);
    ePc[h] = canonical_mod_vector(bnfisprincipal(bnf, idealhnf(nf, dec[pairs[h][2]]), 0), cyc);
    print("pair_class_", h, "_P=", eP[h], " Pc=", ePc[h]);
  );
  print("prime_class_vectors_ms=", gettime());

  base = k + 1;
  record_count = base^pair_count;
  print("J_record_count=", record_count);

  gettime();
  exponents = vector(record_count);
  classes = vector(record_count);
  for (idx = 1, record_count,
    exponents[idx] = decode_exponents(idx - 1, base, pair_count);
    classes[idx] = class_of_exponents(exponents[idx], eP, ePc, k, cyc);
  );
  print("J_class_enumeration_ms=", gettime());

  print("collision_search_start");
  gettime();
  reported = 0;
  done = 0;
  for (li = 1, record_count - 1,
    if (done, break());
    for (ri = li + 1, record_count,
      if (classes[li] == classes[ri],
        reported = reported + 1;
        delta = vector(pair_count, h, exponents[li][h] - exponents[ri][h]);
        print("collision_", reported);
        print("  left_index=", li, " right_index=", ri);
        print("  left_exponents=", exponents[li]);
        print("  right_exponents=", exponents[ri]);
        print("  delta=", delta);
        print("  class=", classes[li]);

        JL = build_J(nf, dec, pairs, exponents[li], k);
        JR = build_J(nf, dec, pairs, exponents[ri], k);
        ratio = idealdiv(nf, JL, JR);
        principal = bnfisprincipal(bnf, ratio, 3);
        print("  principal_class_vector=", principal[1]);
        gam = principal[2];
        gam_c = nfgaloisapply(nf, cm, gam);
        gam_emb = nfeltembed(nf, gam)[1];
        gam_c_emb = nfeltembed(nf, gam_c)[1];
        u_emb = gam_emb / gam_c_emb;
        print("  gamma=", gam);
        print("  u_embedding=", u_emb);
        print("  abs_u_minus_1=", abs(abs(u_emb) - 1));
        if (reported >= max_report,
          done = 1;
          break();
        );
      );
    );
  );
  print("collisions_reported=", reported);
  print("collision_search_and_principalization_ms=", gettime());
};

main();
