# Layoffs Data Analysis

## Project Overview
This notebook explores and analyzes layoffs data by performing various transformations and visualizations using **Pandas** and **Plotly**. The key insights derived from this analysis include identifying companies, locations, and industries most impacted by layoffs. Additionally, we investigate the relationship between funds raised and layoffs.

## Key Observations
1. **Top 10 companies that laid off the most employees**.
2. **Top 3 companies that laid off the most employees year-wise**
3. **Top 3 locations with the highest layoffs year-wise**.
4. **Top 20 companies that laid off a specific percentage of their employees**.
5. **Top 10 countries with the most layoffs**.
6. **Top 10 locations with the most layoffs in the USA**.
7. **Top locations in India where the most layoffs occurred**.
8. **Stages of company development most impacted by layoffs**.
9. **Industries with the most layoffs**.
10. **Total layoffs year-wise**.
11. **Year-wise layoffs by country**.


## Dataset
The dataset used contains information on layoffs across companies, including the following columns:
- `company`: Name of the company.
- `location`: Location of the company.
- `industry`: Industry category.
- `total_laid_off`: Total number of employees laid off.
- `percentage_laid_off`: Percentage of workforce laid off.
- `date`: Date of layoffs.
- `stage`: Development stage of the company (e.g., Post-IPO, Series C).
- `country`: Country where the company is located.
- `funds_raised`: Total funds raised by the company.

### Example Dataset Snapshot:
| company     | location   | industry   | total_laid_off | percentage_laid_off | date       | stage    | country      | funds_raised |
|-------------|------------|------------|----------------|---------------------|------------|----------|--------------|--------------|
| Northvolt   | Stockholm  | Energy     | 1600           | 0.20                | 2025-09-23 | Unknown  | Sweden       | 13800        |
| Drata       | San Diego  | Security   | 40             | 0.09                | 2024-09-26 | Series C | United States| 328          |
| Moov        | Cedar Falls| Finance    | 50             | NaN                 | 2024-09-25 | Series B | United States| 77           |

## Data Cleaning and Transformation
- **Handling Missing Values**: Missing values in columns like `total_laid_off`, `percentage_laid_off`, and `funds_raised` were filled with 0 to avoid errors during analysis.
- **Duplicate Entries**: The data contained duplicates where companies had multiple records across different dates. A clean dataset was created by aggregating total layoffs for each company.


## Visualizations

![image](https://github.com/user-attachments/assets/130f51da-f000-4404-bc34-216332d14540)

![image](https://github.com/user-attachments/assets/9f5cc37a-93f5-45ae-87e6-51bbc2850b9c)

![image](https://github.com/user-attachments/assets/30534bb0-d53c-4fc7-93e9-2f1d82a75291)

![image](https://github.com/user-attachments/assets/ef97cd8c-7633-497e-b1cd-2544f886ba48)

![image](https://github.com/user-attachments/assets/d5c37bbe-4a09-4678-bcdc-5a48eff68946)

![image](https://github.com/user-attachments/assets/47d54271-5e7f-40da-ae3e-ee1e04479444)

![image](https://github.com/user-attachments/assets/0de90957-5b74-40f2-ab10-a099ff21dff2)

![image](https://github.com/user-attachments/assets/76745d74-b09c-4d6b-af0f-790ae6952911)

![image](https://github.com/user-attachments/assets/2d18ffe0-068f-4df5-99b9-0ef584fb517a)

![image](https://github.com/user-attachments/assets/a94135ba-3841-4799-9dc7-c2cbaefbf6ab)

![image](https://github.com/user-attachments/assets/78c3ed69-449a-4a50-b6ab-856acf7987a7)







