delimiter //

create procedure f2b_sp_add_host(in pi_host_name varchar(128), in pi_host_ip varchar(64))
 begin
	insert into f2b_hosts (
	         host_name
	       , host_ip	
	)
	values (
		 pi_host_name
	       , pi_host_ip
	); 
 end //

create procedure f2b_sp_add_to_whitelist(in pi_allow_ip varchar(64))
 begin
	insert into f2b_whitelist (
	       	 allow_ip	
	)
	values (
	         pi_allow_ip
	); 
 end //

create procedure f2b_sp_add_to_blacklist(in pi_deny_ip varchar(64))
 begin
	insert into f2b_blacklist (
	       	 deny_ip	
	)
	values (
	         pi_deny_ip
	); 
end //

create procedure f2b_sp_log_attack(in pi_attacked_host varchar(128), in pi_attacker_ip varchar(64))
 begin

	declare l_host_id integer;
	declare l_attacker_id integer;
	
	set l_host_id = (select id from f2b_hosts where host_name = pi_attacked_host);

	insert into f2b_attackers (
	         host_id
	       , attacker_ip
	)
	values (
	         l_host_id
	       , pi_attacker_ip
	)
	on duplicate key update last_seen = current_timestamp;

	set l_attacker_id = (select id from f2b_attackers where attacker_ip = pi_attacker_ip);

	insert into f2b_incidents (
	         attacker_id)
	values (
	         l_attacker_id
	);

 end //

delimiter ;
