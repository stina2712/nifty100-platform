# Sprint 2 Retrospective: Financial Ratio Engine

## Summary
* **Pipeline Status**: Successfully processed 1,276 companies.
* **Database**: `financial_ratios` table is fully populated.
* **Testing**: 10/10 KPI formula unit tests passed.

## Formula Decisions & Edge Cases
* **ROCE Carve-Out**: Implemented sector-relative benchmarks for Financials broad_sector companies.
* **CAGR Logic**: Implemented all 6 edge case handlers (e.g., DECLINE_TO_LOSS, TURNAROUND) as per requirements.
* **Anomaly Log**: No discrepancies > 5% found; log marked as verified.

## Manual Spot-Check
Performed manual re-computation of ROE and 5-year Revenue CAGR for 3 companies (TCS, Reliance, HDFC Bank).
* **Variance**: All manual calculations matched database values within < 0.1% tolerance.

## Sign-off
Sprint 2 Exit Criteria met and verified.