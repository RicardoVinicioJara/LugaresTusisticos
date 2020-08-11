from neo4j import GraphDatabase
from pandas import DataFrame


class myneo4j():
    def __init__(self):
        self.driver = GraphDatabase.driver("bolt://localhost:7687", auth=("neo4j", "1004"), encrypted=False)
        self.session = self.driver.session()

    def MyBase(self):
        result = self.session.run("""MATCH (n) return n.name""")
        result = DataFrame(result)
        rest = str(result)
        print(rest)
        return rest

    def hoteles(self, cidudad):
        result = self.session.run("""MATCH ({name : '""" + cidudad + """'})-[CONNECTION]-({name: "Hoteles"})-[*]-(c) RETURN c.name as name""")
        result = DataFrame(result)
        rest = str(result)
        print(rest)
        return rest



    def ComollegoA(self, lugar):
        result = self.session.run("""MATCH (start:Station {name: "Ecuador"}), (end:Station {name: '""" + lugar + """'})
                CALL gds.alpha.shortestPath.astar.stream({
                  nodeQuery: 'MATCH (p:Station) RETURN id(p) AS id',
                  relationshipQuery: 'MATCH (p1:Station)-[r:CONNECTION]->(p2:Station) RETURN id(p1) AS source, id(p2) AS target, r.time AS weight',
                  startNode: start,
                  endNode: end,
                  relationshipWeightProperty: 'weight',
                  propertyKeyLat: 'latitude',
                  propertyKeyLat: 'latitude'
                })
                YIELD nodeId, cost
                RETURN gds.util.asNode(nodeId).name AS station, cost""")
        txtAudio = " Para llegar  " + lugar + "  tiene que seguir el camino de: "
        result = DataFrame(result)
        print(result)
        for r in result[0]:
            txtAudio = txtAudio + " " + r + ","

        return result, txtAudio

    def ComollegoDA(self, l1, l2):
        result = self.session.run("""MATCH (start:Station {name: '""" + l1 + """'}), (end:Station {name: '""" + l2 + """'})
                CALL gds.alpha.shortestPath.stream({
                  nodeProjection: 'Station',
                  relationshipProjection: {
                    ROAD: {
                      type: 'CONNECTION',
                      properties: 'time',
                      orientation: 'UNDIRECTED'
                    }
                  },
                  startNode: start,
                  endNode: end,
                  relationshipWeightProperty: 'time'
                })
                YIELD nodeId, cost
                RETURN gds.util.asNode(nodeId).name AS name""")
        txtAudio = " Para llegar de " + l1 + " hasta " + l2 + " tiene que seguir el camino de: "

        result = DataFrame(result)
        print(result)
        for r in result[0]:
            txtAudio = txtAudio + " " + r + ","
        return result, txtAudio

    def ubicacion(self, cidudad):
        result = self.session.run("""MATCH(n{name: '""" + cidudad + """'}) RETURN n.latitude, n.longitude""")
        result = DataFrame(result)
        txt = "https://maps.google.com/?q="
        for r in result[0]:
           txt = txt +""+ str(r) +""+ ","
        for r in result[1]:
           txt = txt +""+ str(r)
        return txt


if __name__ == '__main__':
    my = myneo4j()
    rest = myneo4j.ubicacion(my, "Cuenca")
    print(rest)

