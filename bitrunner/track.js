/** @param {NS} ns */
export async function main(ns) {
    const st = ns.stock
  
    const syms = st.getSymbols()
  
    while (true) {
      let tim = ns.getResetInfo().lastAugReset
      let fnames = []
      let ofiles = []
      for (let sym of syms) {
        fnames[sym] = `stocks/stock-${sym}-${tim}.js`
        ofiles[sym] = new File([], fnames[sym]);
        ns.write(fnames[sym], 'ask,bid,spread,p1,p2,p3,p4\n', 'w')
      }
  
      let intervals = 0
      while (intervals < 3600) {
        //?maybe we should track position too to see impacts on first order prediction
        for (let sym of syms) {
          let ask = st.getAskPrice(sym)
          let bid = st.getBidPrice(sym)
          let spread = ask - bid
          let pos = st.getPosition(sym)
          ns.write(fnames[sym], `${ask},${bid},${spread},${pos[0]},${pos[1]},${pos[2]},${pos[3]}\n`, "a");
        }
        intervals++
        await ns.sleep(6000)
      }
      await ns.sleep(1000 * 3600)
    }
  }