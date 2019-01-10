
    const host = location.host

    const Store = {
      ids: null,
      fetchIds: function () {
        console.log(`http://${host}/ids`)
        m.request(`http://${host}/ids`)   // `http://localhost:3000/ids`
          .then(function (data) {
            Store.ids = data
          })
      },
      saveRec(nrec) {
        console.log(JSON.stringify(nrec, 0, 2))
        let id = nrec.id
        m.request({
          method: 'put',
          url: `http://${host}/ids/${id}`,
          data: nrec
        }).then(function (data) {
          m.redraw()
        })
      },
      setId: function(id, selected_id) {
        let newrec = Store.ids.find(function (rec) {
          return rec.id == id
        })
        // console.log('newrec', JSON.stringify(newrec, 0, 2));
        if (newrec) {
          if (newrec.selected == selected_id) {
            delete newrec.selected
          } else {
            newrec['selected'] = selected_id
          }
          Store.saveRec(newrec)
        } else {
          alert("Couldn't find company with id: " + id)
        }
      }
    }

    const CompanyListing = {
      handleIdSelection: function(recid, refid) {
        return function() {
          Store.setId(recid, refid)
        }
      },
      view: function (vnode) {
        let ids = vnode.attrs.ids
        return m('table.table.table-bordered',
          ids.map(function (rec) {
            return m('tr',
              m('td.company_name', rec.name),
              m('td',
                rec.refs.map(function (ref) {
                  var current = (rec.selected == ref.id) ? 'btn-primary' : 'btn-outline-info'
                  return [
                    m(`button.btn.btn-sm.${current}`,
                      {onclick: CompanyListing.handleIdSelection(rec.id, ref.id),},
                      `${ref.id} (${ref.count})`),
                    m.trust(' &nbsp; ')
                  ]
                })))
          })
        )
      }
    }

    const SMALLEST = Symbol('Smallest')
    const LARGEST = Symbol('Largest')
    const MOSTUSED = Symbol('Mostused')
    const LEASTUSED = Symbol('Leastused')

    const Options = {
      setIDs(opt) {
        return function() {
          Store.ids.forEach(rec => {
            let newid = 0
            if (opt === SMALLEST) {
              newid = Math.min(...rec.refs.map(r => r.id))
            } else if (opt === LARGEST) {
              newid = Math.max(...rec.refs.map(r => r.id))
            } else if (opt === MOSTUSED) {
              newid = Math.max(...rec.refs.map(r => r.count))
            } else if (opt === LEASTUSED) {
              newid = Math.min(...rec.refs.map(r => r.count))
            }
            rec.selected = newid
            Store.saveRec(rec)
          })
        }
      },
      view() {
        return m('div.my-2',
          m('span', 'Set ID: '),
          m('button.btn.btn-outline-secondary.btn-sm.mr-2', {onclick:Options.setIDs(SMALLEST)}, 'Smallest ID'),
          m('button.btn.btn-outline-secondary.btn-sm.mr-2', {onclick:Options.setIDs(LARGEST)}, 'Largest ID'),
          m('button.btn.btn-outline-secondary.btn-sm.mr-2', {onclick:Options.setIDs(MOSTUSED)}, 'Most used'),
          m('button.btn.btn-outline-secondary.btn-sm', {onclick:Options.setIDs(LEASTUSED)}, 'Least used'))
      }
    }

    const App = {
      oncreate: Store.fetchIds,
      view() {
        return (Store.ids)
        ? [
            m('h4.header', 'Company ID selector'),
            m(Options),
            m(CompanyListing, {
              ids: Store.ids
            })
          ]
        : [
            m('p.header', 'Loading ...'),
            m('hr'),
            m('p.small', 'Company ID selector. Mithril ' + m.version)
          ]
      }
    }

    const app = m.mount(document.getElementById('arena'), App)
