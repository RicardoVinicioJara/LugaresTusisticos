#MATCH (n) OPTIONAL MATCH (n)-[r]-() DELETE n,r

CREATE (a:Station{name:"Ecuador" , latitude: -1.465068, longitude: -78.683544}),

       (b:Station{name:"Galapagos", latitude: -1.800773, longitude: -79.529088}),
       (c:Station{name:"Cuenca", latitude: -0.927780, longitude: -78.606022}),
       (d:Station{name:"Quito", latitude: 0.238651, longitude: -78.261538}),
       (e:Station{name:"Cañar", latitude: -0.967627, longitude: -80.711587}),
       (f:Station{name:"Chimborazo", latitude: -0.237749, longitude: -79.173844}),
       (g:Station{name:"Cotopaxi", latitude: -1.800773, longitude: -79.52908}),

       (h:Station{name:"Turismo", latitude: -1.017384, longitude: -79.189592}),
       (i:Station{name:"Hoteles", latitude: -1.017384, longitude: -79.189592}),
 
      (j:Station{name:"Parque de Galapagos", latitude: -0.580414, longitude: -90.342608}),
(k:Station{name:"Galapagos Best Hostel", latitude: -0.723092, longitude: -90.315015}),
(l:Station{name:"Hotel San Cristobal", latitude: -0.897648, longitude: -89.607971}),
(m:Station{name:"Sun Island Hostel", latitude: -0.956689, longitude: -90.967258}),
(n:Station{name:"Casita de la Playa", latitude: -0.957290, longitude: -90.967408}),

      (o:Station{name:"Parque Nacional el Cajas", latitude: -1.801444, longitude: -79.533376}),
(p:Station{name:"Hosteria dos Choreras", latitude: -2.783978, longitude: -79.168266}),
(q:Station{name:"Las cabañas del Pescador", latitude: -2.804136, longitude: -79.157741}),
(r:Station{name:"Estancia San Juan", latitude: -2.777887, longitude: -79.169003}),

      (s:Station{name:"Monumento Mitad del Mundo", latitude: -0.237749, longitude: -79.173844}),
(t:Station{name:"Hostal Mitad Del Mundo", latitude: -0.006345, longitude: -78.449836}),
(u:Station{name:"Hotel Dos Hemisferios", latitude: -0.006158, longitude: -78.446095}),
(v:Station{name:"Hostal Sol y Luna", latitude: 0.006542, longitude: -78.446369}),
(w:Station{name:"La cas de Campo", latitude: 0.004542, longitude: -78.446769}),

      (x:Station{name:"Ruinas de Ingapirca", latitude: -2.527105, longitude: -78.869635}),
(y:Station{name:"Hosteria la Condeza", latitude: -2.527605, longitude: -78.918655}),
(z:Station{name:"Hospedaje el Castillo", latitude: -2.541890, longitude: -78.872635}),
(aa:Station{name:"Posada Ingapirca", latitude: -2.551890, longitude: -78.902635}),
(bb:Station{name:"Cuna del Sol", latitude: -2.561890, longitude: -78.882635}),

      (cc:Station{name:"Volcan Chimborazo", latitude: -1.516734, longitude: -79.529088}),
(dd:Station{name:"Hotel San Andres", latitude: -1.519882, longitude:  -78.837682}),
(ee:Station{name:"Chimborazo Lodge", latitude: -1.518634, longitude: -78.835809}),
(ff:Station{name:"Hosteria la Andaluza", latitude: -1.616734, longitude: -79.729088}),

      (gg:Station{name:"Laguna Quilatoa", latitude: -0.867713, longitude: -79.533376}),
(hh:Station{name:"Hosteria Alpaka", latitude:-0.878713, longitude: -78.917429}),
(ii:Station{name:"Hosteria Alpaka Quilotea", latitude: -0.883713, longitude: -79.817429}),
(jj:Station{name:"Runa Wasi Quilotoa", latitude: -0.868713, longitude: -78.937429}),
(kk:Station{name:"Hotal Chukirawa", latitude: -0.870713, longitude: -79.887429}),

       (ll:Station{name:"Turismo", latitude: -1.017384, longitude: -79.189592}),
       (mm:Station{name:"Hoteles", latitude: -1.017384, longitude: -79.189592}),

       (nn:Station{name:"Turismo", latitude: -1.017384, longitude: -79.189592}),
       (oo:Station{name:"Hoteles", latitude: -1.017384, longitude: -79.189592}),

       (pp:Station{name:"Turismo", latitude: -1.017384, longitude: -79.189592}),
       (qq:Station{name:"Hoteles", latitude: -1.017384, longitude: -79.189592}),

       (rr:Station{name:"Turismo", latitude: -1.017384, longitude: -79.189592}),
       (ss:Station{name:"Hoteles", latitude: -1.017384, longitude: -79.189592}),

       (tt:Station{name:"Turismo", latitude: -1.017384, longitude: -79.189592}),
       (uu:Station{name:"Hoteles", latitude: -1.017384, longitude: -79.189592}),
     

 (a)-[:CONNECTION {time: 398}]->(b),  
 (a)-[:CONNECTION {time: 1}]->(c),
 (a)-[:CONNECTION {time: 1}]->(d),
 (a)-[:CONNECTION {time: 1}]->(e),
 (a)-[:CONNECTION {time: 1}]->(f),
 (a)-[:CONNECTION {time: 1}]->(g),

 (b)-[:CONNECTION {time: 1}]->(h),
 (b)-[:CONNECTION {time: 1}]->(i),

 (c)-[:CONNECTION {time: 1}]->(ll),
 (c)-[:CONNECTION {time: 1}]->(mm),

 (d)-[:CONNECTION {time: 1}]->(nn),
 (d)-[:CONNECTION {time: 1}]->(oo),

 (e)-[:CONNECTION {time: 1}]->(pp),
 (e)-[:CONNECTION {time: 1}]->(qq),

 (f)-[:CONNECTION {time: 1}]->(rr),
 (f)-[:CONNECTION {time: 1}]->(ss),

 (g)-[:CONNECTION {time: 1}]->(tt),
 (g)-[:CONNECTION {time: 1}]->(uu),

 (h)-[:CONNECTION {time: 1}]->(j),

 (i)-[:CONNECTION {time: 1}]->(k),
 (i)-[:CONNECTION {time: 1}]->(l),
 (i)-[:CONNECTION {time: 1}]->(m),
 (i)-[:CONNECTION {time: 1}]->(n),

 (ll)-[:CONNECTION {time: 1}]->(o),
 (mm)-[:CONNECTION {time: 1}]->(p),
 (mm)-[:CONNECTION {time: 1}]->(q),
 (mm)-[:CONNECTION {time: 1}]->(r),

 (nn)-[:CONNECTION {time: 1}]->(s),
 (oo)-[:CONNECTION {time: 1}]->(t),
 (oo)-[:CONNECTION {time: 1}]->(u),
 (oo)-[:CONNECTION {time: 1}]->(v),
 (oo)-[:CONNECTION {time: 1}]->(w),

 (pp)-[:CONNECTION {time: 1}]->(x),
 (qq)-[:CONNECTION {time: 1}]->(y),
 (qq)-[:CONNECTION {time: 1}]->(z),
 (qq)-[:CONNECTION {time: 1}]->(aa),
 (qq)-[:CONNECTION {time: 1}]->(bb),

 (rr)-[:CONNECTION {time: 1}]->(cc),
 (ss)-[:CONNECTION {time: 1}]->(dd),
 (ss)-[:CONNECTION {time: 1}]->(ee),
 (ss)-[:CONNECTION {time: 1}]->(ff),

 (tt)-[:CONNECTION {time: 1}]->(gg),
 (uu)-[:CONNECTION {time: 1}]->(hh),
 (uu)-[:CONNECTION {time: 1}]->(ii),
 (uu)-[:CONNECTION {time: 1}]->(jj),
 (uu)-[:CONNECTION {time: 1}]->(kk)
