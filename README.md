Un attacco DDoS (Distributed Denial of Service) è un tipo di attacco informatico in cui numerosi sistemi distribuiti, come computer o dispositivi compromessi, inviano una grande quantità di traffico verso un server o una rete bersaglio. 
L’obiettivo è sovraccaricare il target, impedendo agli utenti legittimi di accedere ai servizi. Questo tipo di attacco è pericoloso perché può far rallentare o interrompere completamente un sito web, un’applicazione o un'intera infrastruttura di rete.

Cosa fa questo codice
Il codice serve per un attacco chiamato UDP flood, un tipo specifico di attacco DDoS che usa pacchetti UDP (User Datagram Protocol) per generare traffico verso una destinazione specifica.

Ecco un breve riassunto delle operazioni:

Creazione di un socket UDP: Viene creato un socket per inviare pacchetti di dati casuali tramite UDP.
Generazione dei dati: Crea un pacchetto di 1024 byte di dati casuali.
Invio dei pacchetti: Invia il numero di pacchetti specificato (num_packets) all’indirizzo IP e alla porta forniti dall’utente.
Ripetizione del processo: Questo codice può essere usato in un ciclo continuo per inviare più pacchetti, simulando così un flood di traffico.
