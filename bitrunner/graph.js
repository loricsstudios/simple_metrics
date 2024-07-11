/** @param {NS} ns */
export async function main(ns) {
  //let outputFile=new File("output.csv",);
  // const outputFile = "output.csv";
  ns.tail();
  // ns.write("output.txt", "security,money,growth\n", "w");
  let host = ns.args[0] ? ns.args[0] : "n00dles";
  let plot_id = ns.args[1] ? ns.args[1] : 1;
  const plotscript = "dist/plot.js"
  const origin = ns.getServer().hostname
  const minsec = ns.getServerMinSecurityLevel(host);
  const maxsec = 100;
  const maxmoney = ns.getServerMaxMoney(host);
  const logmult = 2;

  let dataframe = {
    'plot_title': `Metrics for node ${host}`,
    'x_label': 'Time',
    'y_label': 'Value',
    'y_range': (0, 100),
    'legend_location': 'upper right',
    
    'data_sets': {
        'set1': {'color': 'r', 'label': 'Target server security', 'marker': 'o'},
        'set2': {'color': 'b', 'label': 'Target server money', 'marker': 'o'}, //s
        'set3': {'color': 'g', 'label': 'Overall Money', 'marker': 'o'}, //s
       
        
    },
   
  }

  ns.exec(plotscript, origin, 1, `config/${plot_id}`, JSON.stringify(dataframe));

  
  // ns.printf("SL,MA");
  while (true) {
    // ns.printf("%d,%d", ns.getServerSecurityLevel(host), ns.getServerMoneyAvailable(host));
    // ns.tprint(JSON.stringify());
    let since = Math.floor((Date.now()-ns.getResetInfo().lastAugReset)/1000);
    let cur_sec = ns.getServerSecurityLevel(host);
    let cur_money = ns.getServerMoneyAvailable(host);
    
    dataframe = { "x": since, "y": Math.floor(((cur_sec-minsec)/maxsec)*100)};
    ns.exec(plotscript, origin, 1, `id/${plot_id}/set/set1`, JSON.stringify(dataframe));
    

    dataframe = { "x": since, "y": Math.floor((cur_money/maxmoney)*100) };
    ns.exec(plotscript, origin, 1, `id/${plot_id}/set/set2`, JSON.stringify(dataframe));
    
    
    dataframe = { "x": since, "y": Math.log(ns.getPlayer().money)*logmult};
    ns.exec(plotscript, origin, 1, `id/${plot_id}/set/set3`, JSON.stringify(dataframe));
    

    await ns.sleep(1000); //graph data with 0.1 sec frequency
  }

}