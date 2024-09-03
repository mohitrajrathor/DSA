// computing character frequency in javascript 

// classes 
class DefualtMap extends Map {
    constructor(defaultvalue) {
        super()
        this.defaultvalue = defaultvalue
    }

    get(key) {
        if (this.has(key)) {
            return super.get(key)
        }
        else {
            return this.defaultvalue
        }
    }
}


class Histogram {
    constructor() {
        this.lettercounts = new DefualtMap(0)
        this.totalletters = 0
    }

    add(text) {
        text = text.replace(/\s/g, "").toUpperCase()

        // loop chars
        for(let character of text) {
            let count = this.lettercounts.get(character)
            this.lettercounts.set(character, count+1)
            this.totalletters++
        }

    }

    toString()  {
        let entries = [...this.lettercounts]

        entries.sort((a,b)=>{
            if (a[i] === b[1]) {
                return a[0] < b[0] ? -1 : 1
            }
            else {
                return b[1] - a[1]
            }
        })

        for (let entry of entries) {
            entry[1] = entry[1] / this.totalletters*100
        }

        entries = entries.filter(entry => entry[1] >= 1)

        let lines = entries.map(
            ([l,n]) => `${l} ${"#".repeat(Math.round(n))} ${n.toFixed(2)}%`
        )

        return lines.join("\n")
    }

}

async function histogramFromStdin() {
    process.stdin.setEncoding("utf-8")
    let histogram = new Histogram()
    for await (let chunk of process.stdin) {
        histogram.add(chunk)
    } 
    return Histogram
}


histogramFromStdin().then(histogram => { console.log(histogram.toString())})