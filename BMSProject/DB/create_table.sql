use projectdb;

## 테이블 비우기
DROP TABLE IF EXISTS origina;
DROP TABLE IF EXISTS originb;
DROP TABLE IF EXISTS originc;
DROP TABLE IF EXISTS origind;
DROP TABLE IF EXISTS origine;

DROP TABLE IF EXISTS moduleA_tbl;
DROP TABLE IF EXISTS moduleB_tbl;
DROP TABLE IF EXISTS moduleC_tbl;
DROP TABLE IF EXISTS moduleD_tbl;
DROP TABLE IF EXISTS moduleE_tbl;

DROP TABLE IF EXISTS outlier_tbl;
## 모듈 별 누적 테이블
CREATE TABLE moduleA_tbl (
    timestamp DATETIME NOT NULL,          -- 데이터 수집 시각
    module_id VARCHAR(50) NOT NULL,       -- 모듈 ID

    cell_voltage_v FLOAT NOT NULL,        -- 전압
    cell_temperature_c FLOAT NOT NULL,    -- 온도
    module_current_a FLOAT NOT NULL,      -- 전류
    module_power_kw FLOAT NOT NULL,       -- 전력

    converter_command_pct FLOAT,          -- 0~100%
    soc_pct FLOAT,                        -- SOC (%)
    soh_pct FLOAT,                        -- SOH (%)

    anomaly_score_pct FLOAT DEFAULT 0.00, -- 이상치 점수
    diagnostic_flag INT DEFAULT 0,        -- 0 정상 / 1 경고 / 2 심각

    latency_ms INT DEFAULT NULL           -- 지연시간(ms)
) CHARSET=utf8mb4;



CREATE TABLE moduleB_tbl (
    timestamp DATETIME NOT NULL,          -- 데이터 수집 시각
    module_id VARCHAR(50) NOT NULL,       -- 모듈 ID

    cell_voltage_v FLOAT NOT NULL,        -- 전압
    cell_temperature_c FLOAT NOT NULL,    -- 온도
    module_current_a FLOAT NOT NULL,      -- 전류
    module_power_kw FLOAT NOT NULL,       -- 전력

    converter_command_pct FLOAT,          -- 0~100%
    soc_pct FLOAT,                        -- SOC (%)
    soh_pct FLOAT,                        -- SOH (%)

    anomaly_score_pct FLOAT DEFAULT 0.00, -- 이상치 점수
    diagnostic_flag INT DEFAULT 0,        -- 0 정상 / 1 경고 / 2 심각

    latency_ms INT DEFAULT NULL           -- 지연시간(ms)
) CHARSET=utf8mb4;

CREATE TABLE moduleC_tbl (
    timestamp DATETIME NOT NULL,          -- 데이터 수집 시각
    module_id VARCHAR(50) NOT NULL,       -- 모듈 ID

    cell_voltage_v FLOAT NOT NULL,        -- 전압
    cell_temperature_c FLOAT NOT NULL,    -- 온도
    module_current_a FLOAT NOT NULL,      -- 전류
    module_power_kw FLOAT NOT NULL,       -- 전력

    converter_command_pct FLOAT,          -- 0~100%
    soc_pct FLOAT,                        -- SOC (%)
    soh_pct FLOAT,                        -- SOH (%)

    anomaly_score_pct FLOAT DEFAULT 0.00, -- 이상치 점수
    diagnostic_flag INT DEFAULT 0,        -- 0 정상 / 1 경고 / 2 심각

    latency_ms INT DEFAULT NULL           -- 지연시간(ms)
) CHARSET=utf8mb4;

CREATE TABLE moduleD_tbl (
    timestamp DATETIME NOT NULL,          -- 데이터 수집 시각
    module_id VARCHAR(50) NOT NULL,       -- 모듈 ID

    cell_voltage_v FLOAT NOT NULL,        -- 전압
    cell_temperature_c FLOAT NOT NULL,    -- 온도
    module_current_a FLOAT NOT NULL,      -- 전류
    module_power_kw FLOAT NOT NULL,       -- 전력

    converter_command_pct FLOAT,          -- 0~100%
    soc_pct FLOAT,                        -- SOC (%)
    soh_pct FLOAT,                        -- SOH (%)

    anomaly_score_pct FLOAT DEFAULT 0.00, -- 이상치 점수
    diagnostic_flag INT DEFAULT 0,        -- 0 정상 / 1 경고 / 2 심각

    latency_ms INT DEFAULT NULL           -- 지연시간(ms)
) CHARSET=utf8mb4;

CREATE TABLE moduleE_tbl (
   timestamp DATETIME NOT NULL,          -- 데이터 수집 시각
    module_id VARCHAR(50) NOT NULL,       -- 모듈 ID

    cell_voltage_v FLOAT NOT NULL,        -- 전압
    cell_temperature_c FLOAT NOT NULL,    -- 온도
    module_current_a FLOAT NOT NULL,      -- 전류
    module_power_kw FLOAT NOT NULL,       -- 전력

    converter_command_pct FLOAT,          -- 0~100%
    soc_pct FLOAT,                        -- SOC (%)
    soh_pct FLOAT,                        -- SOH (%)

    anomaly_score_pct FLOAT DEFAULT 0.00, -- 이상치 점수
    diagnostic_flag INT DEFAULT 0,        -- 0 정상 / 1 경고 / 2 심각

    latency_ms INT DEFAULT NULL           -- 지연시간(ms)
) CHARSET=utf8mb4;

## 이상치 테이블
CREATE TABLE outlier_tbl (
    timestamp DATETIME NOT NULL,
    module_id VARCHAR(50) NOT NULL,

    cell_voltage_v FLOAT NOT NULL,
    cell_temperature_c FLOAT NOT NULL,
    module_current_a FLOAT NOT NULL,
    module_power_kw FLOAT NOT NULL,

    converter_command_pct FLOAT,
    soc_pct FLOAT,
    soh_pct FLOAT,

    anomaly_score_pct FLOAT DEFAULT 0.00,
    diagnostic_flag INT DEFAULT 0,
    latency_ms INT DEFAULT NULL,

    p_expected_kw FLOAT,
    power_error_kw FLOAT,
    is_high_power_error BOOLEAN,
    is_low_power_error BOOLEAN,
    power_error_diff INT UNSIGNED,
    is_jump_power_error BOOLEAN,
    mode VARCHAR(20),

    degradation_risk FLOAT,

    temp_rise_rate FLOAT,
    temp_rise_anomaly VARCHAR(20),
    temp_imblance FLOAT,
    tmpe_imblance_anomaly VARCHAR(20),

    energy_input_kwh FLOAT
) CHARSET=utf8mb4;

-- drop table origine;
## 모듈별 원본 테이블

CREATE TABLE origina (
    timestamp DATETIME NOT NULL,          -- 데이터 수집 시각
    module_id VARCHAR(50) NOT NULL,       -- 모듈 ID

    cell_voltage_v FLOAT NOT NULL,        -- 전압
    cell_temperature_c FLOAT NOT NULL,    -- 온도
    module_current_a FLOAT NOT NULL,      -- 전류
    module_power_kw FLOAT NOT NULL,       -- 전력

    converter_command_pct FLOAT,          -- 0~100%
    soc_pct FLOAT,                        -- SOC (%)
    soh_pct FLOAT,                        -- SOH (%)

    anomaly_score_pct FLOAT DEFAULT 0.00, -- 이상치 점수
    diagnostic_flag INT DEFAULT 0,        -- 0 정상 / 1 경고 / 2 심각

    latency_ms INT DEFAULT NULL           -- 지연시간(ms)
) CHARSET=utf8mb4;

CREATE TABLE  originb (
    timestamp DATETIME NOT NULL,          -- 데이터 수집 시각
    module_id VARCHAR(50) NOT NULL,       -- 모듈 ID

    cell_voltage_v FLOAT NOT NULL,        -- 전압
    cell_temperature_c FLOAT NOT NULL,    -- 온도
    module_current_a FLOAT NOT NULL,      -- 전류
    module_power_kw FLOAT NOT NULL,       -- 전력

    converter_command_pct FLOAT,          -- 0~100%
    soc_pct FLOAT,                        -- SOC (%)
    soh_pct FLOAT,                        -- SOH (%)

    anomaly_score_pct FLOAT DEFAULT 0.00, -- 이상치 점수
    diagnostic_flag INT DEFAULT 0,        -- 0 정상 / 1 경고 / 2 심각

    latency_ms INT DEFAULT NULL           -- 지연시간(ms)
) CHARSET=utf8mb4;

CREATE TABLE  originc (
    -- id BIGINT AUTO_INCREMENT PRIMARY KEY,             -- 고유 식별자
    timestamp DATETIME NOT NULL,                      -- 데이터 수집 시각
    module_id VARCHAR(50) NOT NULL,                   -- 해당 배터리 모듈 ID

    cell_voltage_v DECIMAL(10,3) NOT NULL,            -- 전압 (0.000 단위)
    cell_temperature_c DECIMAL(10,2) NOT NULL,        -- 온도 (소수점 2자리)
    module_current_a DECIMAL(10,2) NOT NULL,          -- 전류
    module_power_kw DECIMAL(10,3) NOT NULL,           -- kW 단위 전력

    converter_command_pct DECIMAL(5,2),               -- 0~100% 명령값
    soc_pct DECIMAL(5,2),                             -- State of Charge (%)
    soh_pct DECIMAL(5,2),                             -- State of Health (%)

    anomaly_score_pct DECIMAL(5,2) DEFAULT 0.00,      -- 이상치 점수 %
    diagnostic_flag TINYINT DEFAULT 0,                -- 0 정상 / 1 경고 / 2 심각 (ENUM 대체)
    latency_ms INT DEFAULT NULL                       -- 데이터 지연 시간(ms)
) CHARSET=utf8mb4;

CREATE TABLE  origind (
    timestamp DATETIME NOT NULL,          -- 데이터 수집 시각
    module_id VARCHAR(50) NOT NULL,       -- 모듈 ID

    cell_voltage_v FLOAT NOT NULL,        -- 전압
    cell_temperature_c FLOAT NOT NULL,    -- 온도
    module_current_a FLOAT NOT NULL,      -- 전류
    module_power_kw FLOAT NOT NULL,       -- 전력

    converter_command_pct FLOAT,          -- 0~100%
    soc_pct FLOAT,                        -- SOC (%)
    soh_pct FLOAT,                        -- SOH (%)

    anomaly_score_pct FLOAT DEFAULT 0.00, -- 이상치 점수
    diagnostic_flag INT DEFAULT 0,        -- 0 정상 / 1 경고 / 2 심각

    latency_ms INT DEFAULT NULL           -- 지연시간(ms)
) CHARSET=utf8mb4;

CREATE TABLE  origine (
    timestamp DATETIME NOT NULL,          -- 데이터 수집 시각
    module_id VARCHAR(50) NOT NULL,       -- 모듈 ID

    cell_voltage_v FLOAT NOT NULL,        -- 전압
    cell_temperature_c FLOAT NOT NULL,    -- 온도
    module_current_a FLOAT NOT NULL,      -- 전류
    module_power_kw FLOAT NOT NULL,       -- 전력

    converter_command_pct FLOAT,          -- 0~100%
    soc_pct FLOAT,                        -- SOC (%)
    soh_pct FLOAT,                        -- SOH (%)

    anomaly_score_pct FLOAT DEFAULT 0.00, -- 이상치 점수
    diagnostic_flag INT DEFAULT 0,        -- 0 정상 / 1 경고 / 2 심각

    latency_ms INT DEFAULT NULL           -- 지연시간(ms)
) CHARSET=utf8mb4;

desc modulea_tbl;
show tables;

