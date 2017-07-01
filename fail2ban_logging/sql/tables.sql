create table `f2b_hosts` (
       `id` integer not null auto_increment,
       `host_name` varchar(128) not null,
       `host_ip` varchar(64) not null,
       primary key (`id`),
       unique key (`host_name`, `host_ip`)
);

create table `f2b_attackers` (
       `id` integer not null auto_increment,
       `host_id` integer not null, 
       `attacker_ip` varchar(64) not null,
       `frist_seen` timestamp not null default current_timestamp,
       `last_seen` timestamp not null  default current_timestamp,
       primary key (`id`),
       unique key (`attacker_ip`)
);

create table `f2b_incidents` (
       `id` integer not null auto_increment,
       `attacker_id` integer not null,
       `occurred` timestamp not null default current_timestamp,
       primary key (`id`),
       unique key(`attacker_id`, `occurred`)
);

create table `f2b_blacklist` (
       `id` integer not null auto_increment,
       `deny_ip` varchar(64) not null,
       primary key (`id`),
       unique key (`deny_ip`)
);

create table `f2b_whitelist` (
       `id` integer not null auto_increment,
       `allow_ip` varchar(64) not null,
       primary key (`id`),
       unique key (`allow_ip`)       
);
