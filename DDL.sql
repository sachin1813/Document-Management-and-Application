
CREATE TABLE public.roles (
	role_code varchar(50) NOT NULL,
	role_name varchar(200) NOT NULL,
	status varchar(2) NOT NULL,
	CONSTRAINT roles_pkey PRIMARY KEY (role_code)
);


CREATE TABLE public.users (
	user_id uuid DEFAULT gen_random_uuid() NOT NULL,
	username varchar(50) NOT NULL,
	login_id varchar(100) NOT NULL,
	"password" varchar(255) NOT NULL,
	"name" varchar(100) NULL,
	user_type varchar(20) NULL,
	status varchar(5) NULL,
	CONSTRAINT users_login_id_key UNIQUE (login_id),
	CONSTRAINT users_pkey PRIMARY KEY (user_id),
	CONSTRAINT users_user_type_check CHECK (((user_type)::text = ANY (ARRAY[('ADMIN'::character varying)::text, ('VIEWER'::character varying)::text, ('EDITOR'::character varying)::text])))
);


CREATE TABLE public.documents (
	doc_id uuid DEFAULT gen_random_uuid() NOT NULL,
	title varchar(255) NOT NULL,
	description text NULL,
	uploaded_by uuid NULL,
	upload_time timestamp DEFAULT now() NULL,
	file_path text NOT NULL,
	status varchar(20) NULL,
	CONSTRAINT documents_pkey PRIMARY KEY (doc_id),
	CONSTRAINT documents_uploaded_by_fkey FOREIGN KEY (uploaded_by) REFERENCES public.users(user_id) ON DELETE SET NULL
);


CREATE TABLE public.ingestion_jobs (
	job_id uuid DEFAULT gen_random_uuid() NOT NULL,
	triggered_by uuid NULL,
	doc_id uuid NULL,
	status varchar(20) DEFAULT 'Pending'::character varying NULL,
	created_at timestamp DEFAULT now() NULL,
	updated_at timestamp DEFAULT now() NULL,
	logs text NULL,
	CONSTRAINT ingestion_jobs_pkey PRIMARY KEY (job_id),
	CONSTRAINT ingestion_jobs_status_check CHECK (((status)::text = ANY (ARRAY[('QUEUED'::character varying)::text, ('IN_PROGRESS'::character varying)::text, ('SUCCESS'::character varying)::text, ('FAILURE'::character varying)::text]))),
	CONSTRAINT ingestion_jobs_doc_id_fkey FOREIGN KEY (doc_id) REFERENCES public.documents(doc_id) ON DELETE SET NULL,
	CONSTRAINT ingestion_jobs_triggered_by_fkey FOREIGN KEY (triggered_by) REFERENCES public.users(user_id) ON DELETE SET NULL
);

CREATE TABLE public.user_oauth (
	id uuid DEFAULT gen_random_uuid() NOT NULL,
	user_id uuid NULL,
	login_id varchar(100) NULL,
	"token" text NOT NULL,
	logged_in timestamp DEFAULT now() NULL,
	expires_in timestamp NULL,
	CONSTRAINT user_oauth_pkey PRIMARY KEY (id),
	CONSTRAINT user_oauth_user_id_fkey FOREIGN KEY (user_id) REFERENCES public.users(user_id) ON DELETE CASCADE
);


CREATE TABLE public.user_roles (
	role_code varchar(50) NULL,
	user_id uuid NULL,
	CONSTRAINT user_roles_role_code_fkey FOREIGN KEY (role_code) REFERENCES public.roles(role_code) ON DELETE CASCADE,
	CONSTRAINT user_roles_user_id_fkey FOREIGN KEY (user_id) REFERENCES public.users(user_id) ON DELETE CASCADE
);