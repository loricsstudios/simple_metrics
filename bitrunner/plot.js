/** @param {NS} ns */
export async function main(ns) {
    // where to send the request
    let endpoint = ns.args[0];
    // JSON.strigify preprocessed data
    let dataframe = ns.args[1];
    let ret = ""
    
    try {
      await fetch(`http://localhost:8000/${endpoint}`, {
        method: "POST",
        body: dataframe,
        headers: {
          "Content-type": "application/json; charset=UTF-8"
        }
  
      }).then((response) => response.json())
        .then((json) => (ret = json))
    } catch (e) {
      ns.tprintf(JSON.stringify(e));
    }
    
    return JSON.stringify(ret)
  }