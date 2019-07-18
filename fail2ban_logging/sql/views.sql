create view f2b_v_banlist 
as
	select banned.ip as ip from
	(
	   select attacker_ip as ip from f2b_attackers
		  union
	   select deny_ip as ip from f2b_blacklist
	) banned
	where banned.ip not in ( select allow_ip as ip from f2b_whitelist ); 
