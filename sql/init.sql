CREATE SCHEMA IF NOT EXISTS nsi;

CREATE TABLE IF NOT EXISTS nsi.raw_medical_organizations (
    record_hash TEXT PRIMARY KEY,

    org_id TEXT,
    oid TEXT,

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

    source_version TEXT,
    record_source TEXT DEFAULT 'nsi.rosminzdrav.ru',

    loaded_at TIMESTAMPTZ DEFAULT NOW(),

    raw_payload JSONB NOT NULL
);