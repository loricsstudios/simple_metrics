/** @param {NS} ns */
export async function main(ns) {
  
    //show log of what is happening
    ns.tail();
    
    //default target host
    let host = ns.args[0] ? ns.args[0] : "n00dles";
    // which graph to send the data to, defaults to '1'
    let plot_id = ns.args[1] ? ns.args[1] : 1;
    const plotscript = "plot.js"
    const origin = "home"
    const minsec = ns.getServerMinSecurityLevel(host);
    const maxsec = 100;
    const maxmoney = ns.getServerMaxMoney(host);
    const logmult = 2;
  
    let dataframe = {
      'plot_title': `Metrics for node ${host}`,
      'x_label': 'Time',
      'y_label': 'Value',
      
      'data_sets': {
          'set1': {'color': 'r', 'label': 'Target server security', 'marker': 'o'},
          'set2': {'color': 'b', 'label': 'Targer server money', 'marker': 'o'}, //s
          'set3': {'color': 'g', 'label': 'Overall Money', 'marker': 'o'}, //s
          
      },
     
    }
  
    //TBD debug this
    ns.exec(plotscript, origin, 1, "config", JSON.stringify(dataframe));
  
    while (true) {
      // X data - how long since last reset in seconds .. adjust as needed
      let since = Math.floor((Date.now()-ns.getResetInfo().lastAugReset)/1000);
      let cur_sec = ns.getServerSecurityLevel(host);
      let cur_money = ns.getServerMoneyAvailable(host);
      // first metric - how much security over minimum remains on the server
      dataframe = { "x": since, "y": Math.floor(((cur_sec-minsec)/maxsec)*100)};
      ns.exec(plotscript, origin, 1, `id/${plot_id}/set/set1`, JSON.stringify(dataframe));
      // second metric - how much money does the server have accumulated of the maximum it can hold
      dataframe = { "x": since, "y": Math.floor((cur_money/maxmoney)*100) };
      ns.exec(plotscript, origin, 1, `id/${plot_id}/set/set2`, JSON.stringify(dataframe));
      // third metric - natural logarithm of the money player has (is not linear progression so keep that in mind)
      dataframe = { "x": since, "y": Math.log(ns.getPlayer().money)*logmult};
      ns.exec(plotscript, origin, 1, `id/${plot_id}/set/set3`, JSON.stringify(dataframe));
      //send the data with 1 sec frequency
      await ns.sleep(1000); 
    }
  
  }