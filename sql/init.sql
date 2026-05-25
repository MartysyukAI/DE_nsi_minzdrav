CREATE SCHEMA IF NOT EXISTS nsi;

CREATE TABLE IF NOT EXISTS nsi.raw_medical_organizations (

    raw_record_hash TEXT PRIMARY KEY,

    source_record_id BIGINT,

    org_id TEXT,

    full_name TEXT,
    short_name TEXT,

    inn TEXT,
    kpp TEXT,
    ogrn TEXT,

    address TEXT,

    region_id TEXT,
    region_name TEXT,

    medical_subject_name TEXT,
    organization_type TEXT,

    mo_dept_id TEXT,
    mo_dept_name TEXT,

    create_date DATE,
    modify_date DATE,
    delete_date DATE,
    delete_reason TEXT,

    raw_payload JSONB NOT NULL,

    source_version TEXT,
    record_source TEXT DEFAULT 'nsi.rosminzdrav.ru',

    loaded_at TIMESTAMPTZ DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS nsi.hub_organization (

    hub_org_hash_key VARCHAR(64) PRIMARY KEY,

    org_id TEXT NOT NULL,

    load_date TIMESTAMPTZ DEFAULT NOW(),

    record_source TEXT DEFAULT 'nsi.rosminzdrav.ru'

);

CREATE TABLE IF NOT EXISTS nsi.sat_organization_attrs (

    hub_org_hash_key VARCHAR(64),

    hashdiff VARCHAR(64),

    load_date TIMESTAMPTZ DEFAULT NOW(),

    full_name TEXT,
    short_name TEXT,

    ogrn TEXT,
    inn TEXT,

    address TEXT,

    ved_affiliation_id TEXT,

    inclusion_date DATE,

    record_source TEXT DEFAULT 'nsi.rosminzdrav.ru'

);

CREATE TABLE IF NOT EXISTS nsi.sat_organization_changes (

    change_id SERIAL PRIMARY KEY,

    hub_org_hash_key VARCHAR(64),

    attribute_name TEXT,

    attribute_value TEXT,

    valid_from DATE,

    valid_to DATE,

    loaded_at TIMESTAMPTZ DEFAULT NOW()

);