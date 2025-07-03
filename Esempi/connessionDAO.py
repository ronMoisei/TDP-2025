import mysql.connector
from mysql.connector import errorcode, errors

def get_connection(config):
    """
    Tenta di stabilire una connessione a MySQL e gestisce in modo distinto
    i principali errori di connessione.
    """
    try:
        conn = mysql.connector.connect(**config)
        return conn

    except mysql.connector.Error as err:
        code = err.errno

        # 1) Server spento / non raggiungibile
        if code in (errorcode.CR_CONN_HOST_ERROR, errorcode.CR_CONN_UNAVAILABLE):
            # Reazione applicativa:
            # • Log di livello ERROR
            # • Notifica all’utente di verificare che il servizio MySQL sia in esecuzione
            # • Eventualmente scattare un retry con backoff esponenziale
            print("❌ ERRORE: Impossibile raggiungere il server MySQL.")
            print("   → Verifica che il servizio sia avviato su", config.get("host"))
            # es. schedule_retry(get_connection, config)
            raise

        # 2) Credenziali errate
        elif code == errorcode.ER_ACCESS_DENIED_ERROR:
            # Reazione applicativa:
            # • Log di livello WARN
            # • Mostrare form di login/riconfigurazione credenziali
            print("⚠️ ERRORE: Accesso negato — credenziali non valide.")
            print("   → Controlla user/password nel file di configurazione.")
            # es. prompt_for_credentials()
            raise

        # 3) Database inesistente
        elif code == errorcode.ER_BAD_DB_ERROR:
            # Reazione applicativa:
            # • Log di livello INFO
            # • Offrire all’utente l’opzione di creare il database o correggere il nome
            print(f"ℹ️ ERRORE: Database “{config.get('database')}” non trovato.")
            print("   → Crea il database o modifica il parametro `database`.")
            # es. ask_to_create_database(config["database"])
            raise

        # 4) Superamento del numero massimo di connessioni
        elif code == errorcode.ER_CON_COUNT_ERROR:
            # Reazione applicativa:
            # • Log di livello WARN
            # • Notificare l’utente di attivare un retry ritardato o contattare l’amministratore
            print("⚠️ ERRORE: Troppe connessioni simultanee.")
            print("   → Riprova tra qualche secondo o contatta l’amministratore DB.")
            # es. schedule_retry(get_connection, config, delay=5)
            raise

        # Qualsiasi altro errore
        else:
            print(f"❗ ERRORE MySQL ({code}): {err.msg}")
            raise
