const fs = require("fs")
const fetch = require('node-fetch');

async function createWikiPage(wikiObject) {
    const query = `
        mutation { pages { create(
            title: "${wikiObject.title}"
            description: "${wikiObject.description}"
            content: "${wikiObject.content}"
            editor: "markdown"
            isPublished: ${wikiObject.isPublished}
            isPrivate:  ${wikiObject.isPrivate}
            locale: "${wikiObject.locale}"
            path: "${wikiObject.path}"
            tags: ${wikiObject.tags}
            ) {
            responseResult {
                succeeded
                slug
                message
            }
            page {
                id
            }
            }
        }
        }
    `

    fetch("http://localhost:3000/graphql", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            "Authorization": "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJhcGkiOjIsImdycCI6MSwiaWF0IjoxNjc4NDIwMTgyLCJleHAiOjE3MDk5Nzc3ODIsImF1ZCI6InVybjp3aWtpLmpzIiwiaXNzIjoidXJuOndpa2kuanMifQ.qUojNgD3zEfkmU0Tt3wTKt100vG4Fw_Ld2My5Jw3wYN6e4-hLNYwqPD7H0icFPeSyfPSNM_Ti9KEYbb8ioWQiJfDziG9N9Iy7vKA0K-ClGO8V6n2szo0i-bxciU3WP8NbaZDgxWZyuTtzV4DgbgY8WK96KvKqDm9SG9OywuA3627KnY7OFZmpOwAXjvKs9Ae1NNnZHWfTm6AfAyacYaO9wn3t0SAlG1E99ImDVcgq5NWv2g7LT8QuhPTKy9yj3_YqThpDG_oIqZbWt3VvybqIgDadL4aihqMQY_s1hrFqo-c6uEWIOh572iUI07ZOSglTw7Wx1qeifpSwDdNgMdeAA"
        },
        body: JSON.stringify({
                           query
        })
    }).then(data => {
            console.log(data);
        })

}

function getTopic(name) {
    const dotIndex = name.lastIndexOf('.');
    return name.substring(0, dotIndex).replace(/_/g, ' ');
}

async function main(dir,meta) {
    const files = fs.readdirSync(dir);
    //Get all topics in a directory
    let topicList = []
    for (const names of files) {
        topicList.push(getTopic(names))
    }
    //Read all files and make all keywords reference 
    for (let filesIndex=0;filesIndex < files.length;filesIndex++) {
        let text = fs.readFileSync(dir +"/"+ files[filesIndex], 'utf-8');
        text = text.replace(/(\r\n|\n|\r)/gm, "\\n").split("\r").join("");
        for (let i=0;i < topicList.length;i++) {
            if (filesIndex == i) {
                continue
            }
            text = text.replace(`${topicList[i]}`,`[${topicList[i]}](/en/${files[i]})`)
        }

        const dotIndex = files[filesIndex].lastIndexOf('.');
        const path = files[filesIndex].substring(0, dotIndex)

        const wikiObject = {
        "title" : files[filesIndex],
        "description" : meta.description,
        "content" : text,
        "isPublished" : meta.isPublished,
        "isPrivate" : !meta.isPublished,
        "locale" : meta.locale,
        "path" : `${path}`,
        "tags" : "[]"
        }  

        await createWikiPage(wikiObject);
        console.log(`Create wiki successfully for ${files[filesIndex]} at ${wikiObject.path}`)

    }




}

// (async () => {
//     //const text = fs.readFileSync('./application/data/test.txt', 'utf-8').replace(/[\n\r]/g, '').replace(/\n/g, '\\n');
//     const text = fs.readFileSync('./application/data/transformers/ConvS2S.md', 'utf-8').split('\n').join('\\n').split("\r").join("");
//     //;
//     //const text = fs.readFileSync(, 'utf-8').replace(/\n/g, '\\n');
//     //console.log(text)
//     const wikiObject = {
//     "title" : "ConvS2S",
//     "description" : "Meeting 3/11/2023",
//     "content" : text,
//     "isPublished" : true,
//     "isPrivate" : false,
//     "locale" : "en",
//     "path" : "en/ConvS2S",
//     "tags" : "[]"

//   }  
//   await createWikiPage(wikiObject);
// })();

(async () => {
    //const text = fs.readFileSync('./application/data/test.txt', 'utf-8').replace(/[\n\r]/g, '').replace(/\n/g, '\\n');
    // let text = fs.readFileSync('./application/data/test.txt', 'utf-8');
    // text = text.replace(/(\r\n|\n|\r)/gm, "\\n");
    // //const text = fs.readFileSync(, 'utf-8').replace(/\n/g, '\\n');
    // //console.log(text)
    const metaData = {
    "locale" : "en",
    "title" : "Testing",
    "description" : "Meeting 3/11/2023",
    "isPublished" : true,
    "isPrivate" : false,
  }  
  await main("./application/data/podcast",metaData);
})();