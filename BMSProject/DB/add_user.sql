-- ===================================================
-- 팀원 4명 계정 추가 
-- * @'%' → 어떤 IP에서든 접속 가능 (외부 접속 허용)
-- * 내부망만 허용하려면 예: @'192.168.0.%' 로 변경
-- ===================================================



-- ===================================================
-- 계정 단위 IP 제한 + 윈도우 방화벽에서 IP 제한
-- =================================================== 
CREATE USER 'user1'@'172.30.1.66' IDENTIFIED BY 'user1';
CREATE USER 'user2'@'172.30.1.58' IDENTIFIED BY 'user2';
CREATE USER 'user3'@'172.30.1.99' IDENTIFIED BY 'user3';
-- CREATE USER 'user4'@'203.0.113.13' IDENTIFIED BY 'user4';


-- ======================================================
-- -- user1
-- CREATE USER 'user1'@'%' IDENTIFIED BY 'user1';
-- -- user2
-- CREATE USER 'user2'@'%' IDENTIFIED BY 'user2';
-- -- user3
-- CREATE USER 'user3'@'%' IDENTIFIED BY 'user3';
-- -- user4
-- CREATE USER 'user4'@'%' IDENTIFIED BY 'user4';
-- ======================================================