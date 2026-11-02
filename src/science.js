// N2O4 ⇌ 2 NO2. Extent x per initial mole: Kp=4x²P/(1-x²).
export function equilibrium(pressure,temperature){const K=Math.exp(57000/8.314*(1/298-1/temperature));return Math.sqrt(K/(4*pressure+K));}
export function acidState(concentration,strong){const ka=1.8e-5;const h=strong?concentration:2*ka*concentration/(ka+Math.sqrt(ka*ka+4*ka*concentration));return {fraction:h/concentration,pH:-Math.log10(h)};}
export function gibbs(temperature){return -40-temperature*(-0.12);}
export function nextReview(correct,streak,now=Date.now()){return now+(correct?[1,3,7,14,30][Math.min(streak,4)]:0)*86400000;}
