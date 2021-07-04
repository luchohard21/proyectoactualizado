let DB;

let form = document.querySelector('form');
let patientName = document.querySelector('#patient-name');
let contact = document.querySelector('#contact');
let date = document.querySelector('#date');
let time = document.querySelector('#time');
let symptoms = document.querySelector('#symptoms');
let consultations = document.querySelector('#consultations');
let services = document.querySelector('#services');
let pago = document.querySelector('#pago');

document.addEventListener('DOMContentLoaded', () => {
     // creando la base de datos
     let CitasDB = window.indexedDB.open('consultations', 1);

     // si hay algún error
     CitasDB.onerror = function() {
          console.log('error');
     }

     CitasDB.onsuccess = function() {
     

          
          DB = CitasDB.result;

          showConsultations();
     }

   
     CitasDB.onupgradeneeded = function(e) {
          
          let db = e.target.result;
          
          let objectStore = db.createObjectStore('consultations', { keyPath: 'key', autoIncrement: true } );

        
          objectStore.createIndex('Nombre', 'Nombre', { unique: false } );
          objectStore.createIndex('contacto', 'contacto', { unique: false } );
          objectStore.createIndex('fecha', 'fecha', { unique: false } );
          objectStore.createIndex('hora', 'hora', { unique: false } );
          objectStore.createIndex('detalle', 'detalle', { unique: false } );
          objectStore.createIndex('pago','pago',{unique: false} );

          //console.log('Database ready and fields created!');
     }

     form.addEventListener('submit', addConsultations);

     function addConsultations(e) {
          e.preventDefault();
          let newConsultation = {
               patientname : patientName.value,
             contact : contact.value,
               date : date.value,
            time : time.value,
               symptoms : symptoms.value,
          }
          
          let transaction = DB.transaction(['consultations'], 'readwrite');
          let objectStore = transaction.objectStore('consultations');

          let request = objectStore.add(newConsultation);
                    request.onsuccess = () => {
               form.reset();
          }
          transaction.oncomplete = () => {
               //console.log('New schedule added');

               showConsultations();
          }
          transaction.onerror = () => {
              //console.log();
          }

     }
     function showConsultations() {
       
          while(consultations.firstChild) {
            consultations.removeChild(consultations.firstChild);
          }
         
          let objectStore = DB.transaction('consultations').objectStore('consultations');

          objectStore.openCursor().onsuccess = function(e) {
               
               let cursor = e.target.result;
               if(cursor) {
                    let ConsultationHTML = document.createElement('li');
                    ConsultationHTML.setAttribute('data-consultation-id', cursor.value.key);
                    ConsultationHTML.classList.add('list-group-item');
                    
                 
                    ConsultationHTML.innerHTML = `  
                         <p class="font-weight-bold">Nombre:  <span class="font-weight-normal">${cursor.value.patientname}<span></p>
                          <p class="font-weight-bold">Contacto:  <span class="font-weight-normal">${cursor.value.contact}<span></p>
                         <p class="font-weight-bold">Fecha:  <span class="font-weight-normal">${cursor.value.date}<span></p>
                         <p class="font-weight-bold">Hora:  <span class="font-weight-normal">${cursor.value.time}<span></p>
                         <p class="font-weight-bold">Detalle:  <span class="font-weight-normal">${cursor.value.symptoms}<span></p>
                         <p class="font-weight-bold"> Medio de pago:  <span class="font-weight-normal">${cursor.value.pago}<span></p>
                    `;

                    
                    const cancelBtn = document.createElement('button');
                    cancelBtn.classList.add('btn', 'btn-danger');
                    cancelBtn.innerHTML = 'Cancelar';
                    cancelBtn.onclick = removeConsultation;
               
                 
                    ConsultationHTML.appendChild(cancelBtn);
                 consultations.appendChild(ConsultationHTML);

                    cursor.continue();
               } else {
                    if(!consultations.firstChild) {
                        services.textContent = 'Rellena los campos solicitados';
                         let noSchedule = document.createElement('p');
                         noSchedule.classList.add('text-center');
                         noSchedule.textContent = 'Sin registro todavía';
                      consultations.appendChild(noSchedule);
                    } else {
                        services.textContent = 'Elimina tu registro'
                    }
               }
          }
     }

          function removeConsultation(e) {
       
          let scheduleID = Number( e.target.parentElement.getAttribute('data-consultation-id') );
         
          let transaction = DB.transaction(['consultations'], 'readwrite');
          let objectStore = transaction.objectStore('consultations');
         
          objectStore.delete(scheduleID);

          transaction.oncomplete = () => {
             
               e.target.parentElement.parentElement.removeChild( e.target.parentElement );

               if(!consultations.firstChild) {
                   
                    services.textContent = 'Elimina tu registro';
                   
                   let noSchedule = document.createElement('p');
                  
                   noSchedule.classList.add('text-center');
                   
                   noSchedule.textContent = 'Sin registro todavía';
                
                    consultations.appendChild(noSchedule);
               } else {
                   services.textContent = 'Elimina tu registro'
               }
          }
     }

});