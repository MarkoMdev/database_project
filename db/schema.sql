CREATE TABLE IF NOT EXISTS intercites_regularite (
    id SERIAL PRIMARY KEY,

    jour DATE NOT NULL,
    gare_depart TEXT NOT NULL,
    gare_arrivee TEXT NOT NULL,

    nb_trains_programmes INTEGER,
    nb_trains_circules INTEGER,
    nb_trains_annules INTEGER,
    nb_trains_en_retard INTEGER,

    taux_regularite NUMERIC(6,3),

    ratio_source_trains_a_lheure_par_retard NUMERIC(6,3),
    ratio_recalc_trains_a_lheure_par_retard NUMERIC(6,3),

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
