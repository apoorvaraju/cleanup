const Wade = require('wade')

console.log(typeof(Wade));

const pns = require('../data/party-and-names.json')

const search = Wade(pns.parties)
    // "Apple", "Lemon", "Orange", "Tomato",
    //                  'application', 'My Application', 'myapp', 'mu App']);

// const pattern_id = 16

// const res = search(pns['clean_names'][pattern_id])

// const certainties = res.filter((r) => r.score >= 1)
// console.log(certainties);


// console.log(pns['clean_names'][pattern_id], ':');
// certainties.forEach(r => {
//     console.log(pns.parties[r.index], r.index);
// })

// console.dir(res)

// List of all clean names:
pns['clean_names'].forEach(cn => {
    // console.log(cn);
    const res = search(cn) // pns['clean_names'][pattern_id])

    const certainties = res.filter((r) => r.score >= 1)
    // console.log(certainties);

    console.log('\n', cn) // pns['clean_names'][pattern_id], ':');
    certainties.forEach(r => {
        console.log('\t', pns.parties[r.index]) //, r.index);
    })
})


// [{
//     index: 10,
//     score: 1
// }]
