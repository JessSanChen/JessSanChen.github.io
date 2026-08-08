#!/bin/bash
# Copies your PDFs out of projects-papers/ into the site, with the names the
# project pages expect. Run once from the site directory.
set -e
SRC="${1:-../projects-papers}"
D=content/static
declare -a M=(
 "uberstable.pdf|uberstable.pdf"
 "CS_243_Final_Project (3).pdf|primes.pdf"
 "CS_236r (3).pdf|compute-marketplace.pdf"
 "CS_237_Final_Project (5).pdf|winners-curse.pdf"
 "CS_226_Final_Project.pdf|fairness-gaming.pdf"
 "CS288 Final Project_ RN-SOAR.pdf|rn-soar.pdf"
 "CS_37_Final_Project (2).pdf|claim-denials.pdf"
 "Ec970_Hukou (3).pdf|hukou-reform.pdf"
 "Gov 1982 Term Paper ESSAY.pdf|cross-strait-brain-drain.pdf"
 "Mentorship Final Paper DRAFT 3.pdf|sst-neuroanatomy.pdf"
)
for e in "${M[@]}"; do
  cp "$SRC/${e%%|*}" "$D/${e##*|}" 2>/dev/null && echo "  ok  ${e##*|}" || echo "  MISSING  ${e%%|*}"
done
echo "Now: pip install markdown && python3 build.py"
