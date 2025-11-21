Total rows: 1000

Total columns: 21

Features: 20

Target: 1 = Good, 2 = Bad

Original dataset contains categorical values (A11, A12, etc.).

Numeric version encodes these categories as integers.

Some ordered categorical attributes are encoded as integers.




Feature Descriptions (Column-wise)

| Column | Name                  | Type        | Description                                                                                                                                                |
| ------ | --------------------- | ----------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **1**  | **CheckingStatus**    | Categorical | Status of existing checking account                                                                                                                        |
| **2**  | **DurationMonths**    | Numeric     | Duration of credit in months                                                                                                                               |
| **3**  | **CreditHistory**     | Categorical | Customer’s credit history                                                                                                                                  |
| **4**  | **Purpose**           | Categorical | Purpose of the credit (loan purpose)                                                                                                                       |
| **5**  | **CreditAmount**      | Numeric     | Credit amount in Deutsche Marks                                                                                                                            |
| **6**  | **SavingsStatus**     | Categorical | Status of savings account/bonds                                                                                                                            |
| **7**  | **EmploymentSince**   | Categorical | Years at current employment                                                                                                                                |
| **8**  | **InstallmentRate**   | Numeric     | % of disposable income                                                                                                                                     |
| **9**  | **PersonalStatusSex** | Categorical | Personal status and sex                                                                                                                                    |
| **10** | **OtherDebtors**      | Categorical | Other debtors/guarantors                                                                                                                                   |
| **11** | **ResidenceSince**    | Numeric     | Years living at current residence                                                                                                                          |
| **12** | **Property**          | Categorical | Property type                                                                                                                                              |
| **13** | **Age**               | Numeric     | Age in years                                                                                                                                               |
| **14** | **OtherInstallPlans** | Categorical | Other installment plans                                                                                                                                    |
| **15** | **Housing**           | Categorical | Housing status                                                                                                                                             |
| **16** | **ExistingCredits**   | Numeric     | Number of existing credits at this bank                                                                                                                    |
| **17** | **Job**               | Categorical | Job type                                                                                                                                                   |
| **18** | **PeopleLiable**      | Numeric     | Number of dependents responsible for                                                                                                                       |
| **19** | **Telephone**         | Categorical | Has registered telephone?                                                                                                                                  |
| **20** | **ForeignWorker**     | Categorical | Foreign worker status                                                                                                                                      |
| **21** | **Target**            | Categorical | Credit class: **1 = Good**, **2 = Bad**                                                                                                                    |





Cost Matrix (Original UCI Dataset)

| Actual \ Predicted | Good (1) | Bad (2) |
| ------------------ | -------- | ------- |
| **Good (1)**  | 0            | 1         |
| **Bad (2)**    | 5             | 0         |

Meaning: Predicting a bad customer as good is 5× worse than the opposite.
