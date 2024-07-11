/** @param {NS} ns */
export async function main(ns) {
    const colors = [
      "Black", "Navy", "DarkBlue",
      "MediumBlue", "Blue", "DarkGreen",
      "Green", "Teal", "DarkCyan",
      "DeepSkyBlue", "DarkTurquoise", "MediumSpringGreen",
      "Lime", "SpringGreen", "Aqua",
      "Cyan", "MidnightBlue", "DodgerBlue",
      "LightSeaGreen", "ForestGreen", "SeaGreen",
      "DarkSlateGray", "DarkSlateGrey", "LimeGreen",
      "MediumSeaGreen", "Turquoise", "RoyalBlue",
      "SteelBlue", "DarkSlateBlue", "MediumTurquoise",
      "Indigo", "DarkOliveGreen", "CadetBlue",
      "CornflowerBlue", "RebeccaPurple", "MediumAquaMarine",
      "DimGray", "DimGrey", "SlateBlue",
      "OliveDrab", "SlateGray", "SlateGrey",
      "LightSlateGray", "LightSlateGrey", "MediumSlateBlue",
      "LawnGreen", "Chartreuse", "Aquamarine",
      "Maroon", "Purple", "Olive",
      "Gray", "Grey", "SkyBlue",
      "LightSkyBlue", "BlueViolet", "DarkRed",
      "DarkMagenta", "SaddleBrown", "DarkSeaGreen",
      "LightGreen", "MediumPurple", "DarkViolet",
      "PaleGreen", "DarkOrchid", "YellowGreen",
      "Sienna", "Brown", "DarkGray",
      "DarkGrey", "LightBlue", "GreenYellow",
      "PaleTurquoise", "LightSteelBlue", "PowderBlue",
      "FireBrick", "DarkGoldenRod", "MediumOrchid",
      "RosyBrown", "DarkKhaki", "Silver",
      "MediumVioletRed", "IndianRed", "Peru",
      "Chocolate", "Tan", "LightGray",
      "LightGrey", "Thistle", "Orchid",
      "GoldenRod", "PaleVioletRed", "Crimson", "Gainsboro",
      "Plum", "BurlyWood", "LightCyan",
      "Lavender", "DarkSalmon", "Violet",
      "PaleGoldenRod", "LightCoral", "Khaki",
      "AliceBlue", "HoneyDew", "Azure",
      "SandyBrown", "Wheat", "Beige",
      "WhiteSmoke", "MintCream", "GhostWhite",
      "Salmon", "AntiqueWhite", "Linen",
      "LightGoldenRodYellow", "OldLace", "Red",
      "Fuchsia", "Magenta", "DeepPink",
      "OrangeRed", "Tomato", "HotPink",
      "Coral", "DarkOrange", "LightSalmon",
      "Orange", "LightPink", "Pink",
      "Gold", "PeachPuff", "NavajoWhite",
      "Moccasin", "Bisque", "MistyRose",
      "BlanchedAlmond", "PapayaWhip", "LavenderBlush",
      "SeaShell", "Cornsilk", "LemonChiffon",
      "FloralWhite", "Snow", "Yellow",
      "LightYellow", "Ivory", "White"
    ]
  
    const hexcols = [
      "#000000",
      "#000080",
      "#00008B",
      "#0000CD",
      "#0000FF",
      "#006400",
      "#008000",
      "#008080",
      "#008B8B",
      "#00BFFF",
      "#00CED1",
      "#00FA9A",
      "#00FF00",
      "#00FF7F",
      "#00FFFF",
      "#00FFFF",
      "#191970",
      "#1E90FF",
      "#20B2AA",
      "#228B22",
      "#2E8B57",
      "#2F4F4F",
      "#2F4F4F",
      "#32CD32",
      "#3CB371",
      "#40E0D0",
      "#4169E1",
      "#4682B4",
      "#483D8B",
      "#48D1CC",
      "#4B0082",
      "#556B2F",
      "#5F9EA0",
      "#6495ED",
      "#663399",
      "#66CDAA",
      "#696969",
      "#696969",
      "#6A5ACD",
      "#6B8E23",
      "#708090",
      "#708090",
      "#778899",
      "#778899",
      "#7B68EE",
      "#7CFC00",
      "#7FFF00",
      "#7FFFD4",
      "#800000",
      "#800080",
      "#808000",
      "#808080",
      "#808080",
      "#87CEEB",
      "#87CEFA",
      "#8A2BE2",
      "#8B0000",
      "#8B008B",
      "#8B4513",
      "#8FBC8F",
      "#90EE90",
      "#9370DB",
      "#9400D3",
      "#98FB98",
      "#9932CC",
      "#9ACD32",
      "#A0522D",
      "#A52A2A",
      "#A9A9A9",
      "#A9A9A9",
      "#ADD8E6",
      "#ADFF2F",
      "#AFEEEE",
      "#B0C4DE",
      "#B0E0E6",
      "#B22222",
      "#B8860B",
      "#BA55D3",
      "#BC8F8F",
      "#BDB76B",
      "#C0C0C0",
      "#C71585",
      "#CD5C5C",
      "#CD853F",
      "#D2691E",
      "#D2B48C",
      "#D3D3D3",
      "#D3D3D3",
      "#D8BFD8",
      "#DA70D6",
      "#DAA520",
      "#DB7093",
      "#DC143C",
      "#DCDCDC",
      "#DDA0DD",
      "#DEB887",
      "#E0FFFF",
      "#E6E6FA",
      "#E9967A",
      "#EE82EE",
      "#EEE8AA",
      "#F08080",
      "#F0E68C",
      "#F0F8FF",
      "#F0FFF0",
      "#F0FFFF",
      "#F4A460",
      "#F5DEB3",
      "#F5F5DC",
      "#F5F5F5",
      "#F5FFFA",
      "#F8F8FF",
      "#FA8072",
      "#FAEBD7",
      "#FAF0E6",
      "#FAFAD2",
      "#FDF5E6",
      "#FF0000",
      "#FF00FF",
      "#FF00FF",
      "#FF1493",
      "#FF4500",
      "#FF6347",
      "#FF69B4",
      "#FF7F50",
      "#FF8C00",
      "#FFA07A",
      "#FFA500",
      "#FFB6C1",
      "#FFC0CB",
      "#FFD700",
      "#FFDAB9",
      "#FFDEAD",
      "#FFE4B5",
      "#FFE4C4",
      "#FFE4E1",
      "#FFEBCD",
      "#FFEFD5",
      "#FFF0F5",
      "#FFF5EE",
      "#FFF8DC",
      "#FFFACD",
      "#FFFAF0",
      "#FFFAFA",
      "#FFFF00",
      "#FFFFE0",
      "#FFFFF0",
      "#FFFFFF",
    ]
  
    
    ns.tail();
    
    const snapshot = ns.args[0] ? ns.args[0] : false
    let plot_id = 1;
    const plotscript = "dist/plot.js"
    const origin = ns.getServer().hostname
  
    const st = ns.stock
    let syms = st.getSymbols()
  
    const maxpoints = 3000 // 300
  
    let dataframe = {
      'plot_title': 'Stocks data',
      'x_label': 'Time',
      'y_label': 'Value',
      'data_sets': {},
      'y_range': (100, 0),
      'legend_location': 'upper right',
      'max_points': maxpoints
    }
  
    let maxpp = 0
    for (let i = 0; i < syms.length; i++) {
      dataframe.data_sets[syms[i]] = { 'color': hexcols[i * 3], 'label': syms[i], 'marker': ',' }
      let sp = st.getPrice(syms[i])
      maxpp = sp > maxpp ? sp : maxpp
    }
    //!!!configure the graph
    ns.exec(plotscript, origin, 1, `config/${plot_id}`, JSON.stringify(dataframe));
  
    let since_snapshot = (+snapshot - ns.getResetInfo().lastAugReset)
    //prefeed the data 
    if (snapshot!=false) {
      ns.printf("===")
      ns.printf("=== Snapshot set to : %d", snapshot)
      for (let i = 0; i < syms.length; i++) {
        let fname = `stocks/stock-${syms[i]}-${snapshot}.js`
        ns.printf("== looking for file: %s", fname)
        if (ns.fileExists(fname,'home')) {
          ns.printf("== file exists, reading from it..")
          let fdata = ns.read(fname)
          ns.printf("== got data, splitting it..")
          let lines = fdata.split("\n")
          // ns.printf("== split successful, lines detected: %d", lines.length)
          for (let j=1; j<lines.length-1; j++) {
            //get only the last max_points
            if ((lines.length-j)>maxpoints+1) {
              continue
            }
            //take the first two values, average them and compute relative to max price
            // ns.printf(lines[j]) //debug
            let lsplit = lines[j].split(',')
            let l0 = +lsplit[0]
            let l1 = +lsplit[1]
            let l2 = (l0+l1)/2
            // ns.printf("%f / %f, %f", l0, l1, l2) //debug
            // ns.printf(JSON.stringify(lsplit)) //debug
            dataframe = { "x": (since_snapshot+j*6000)/1000, "y": (l2 / maxpp) * 100 };
            // ns.printf("j: %d, sym: %s, df: %s", j, syms[i],JSON.stringify(dataframe)) //debug
            ns.exec(plotscript, origin, 1, `id/${plot_id}/set/${syms[i]}`, JSON.stringify(dataframe));
            await ns.sleep(1) //maybe? more graceful - looks like it all can't be run in parallel, we might need to implement some batch transfers :(
          }
        }
      }
  
    } 
  
    while (true) {
      let since = Math.floor((Date.now() - ns.getResetInfo().lastAugReset) / 1000);
  
      for (let i = 0; i < syms.length; i++) {
        dataframe = { "x": since, "y": (st.getPrice(syms[i]) / maxpp) * 100 };
        ns.exec(plotscript, origin, 1, `id/${plot_id}/set/${syms[i]}`, JSON.stringify(dataframe));
      }
      //graph data with 6 sec frequency (stock market tick)
      await ns.sleep(6000); 
    }
  
  }