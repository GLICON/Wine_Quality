# Wine Quality
The provided dataset is analyzed to uncover actionable insights into factors influencing red variants of the Portuguese "Vinho Verde" wine, with focus on physiochemical properties such as alcohol, acidity and sulphates. The major objective is to provide data-driven recommendations for wine producers to optimize quality, enhance production processes and inform marketing strategies.

## Table of Contents
- [Project Focus](#project-focus)
- [Data Cleaning and Preparation](#data-cleaning-and-preparation)
- [EDA](#eda)
- [Chemical Drivers of Vinho Verde Wine Quality](#chemical-drivers-of-vinho-verde-wine-quality)
- [High vs Standard Wines](#high-vs-standard-wines)
- [Implications of Wine Quality Distribution](#implications-of-wine-quality-distribution)
- [Production Process Optimisation](#production-process-optimisation)
- [Tools](#tools)
- [Data Sources](#data-sources)


### Project Focus
- Key Drivers of Quality: Which chemical attributes most strongly influence wine ratings, and how can this guide production optimization?
- Target Profiles: How do the chemical profiles of high-quality wines (score ≥7) differ from standard wines (score 5–6), and how can this inform production targets?
- Quality Distribution: What is the distribution of wine quality in our portfolio, and how can this inform inventory management and marketing strategy?

### Data Cleaning and Preparation
In the initial data preparation phase, the following tasks were performed as listed below:

- Checked for missing or null values:No missing value was found.
- Ensured numeric consistency by handling inconsistent data: Columns containing floats were rounded to the best decimal poimt for accurate computations.
- Checked for outliers:
Box and Whisker plot, and IQR formula are used to check for outliers in the physicochemical properties of red wine variants

<img width="415" height="310" alt="WQ_Box plot and whiskers for outliers" src="https://github.com/user-attachments/assets/93f1cef3-9c80-46c4-9529-63288a24b167" />

The IQR formula is used in finding the outliers and are shown below:
fixed acidity (44)
volatile acidity (15)
citric acid
residual sugar (111)
chlorides (74)
free sulfur dioxide (18)
total sulfur dioxide (40)
density (38)
pH (20)
sulphates (43)
alcohol (12)

### EDA
- The correlation function CORREL is used to find the correlation relationship between each property and quality. The result is shown in the table below:

<img width="715" height="293" alt="Screenshot 2025-10-06 at 13 35 31" src="https://github.com/user-attachments/assets/f3083770-0cc0-4a4a-83aa-f3cdffea6293" />

The correlation analysis reveals that alcohol exhibits the strongest positive correlation with quality (0.48), suggesting higher alcohol content enhances perceived quality. Conversely, volatile acidity shows a significant negative correlation, indicating that elevated levels detrimentally impact taste and overall rating, guiding quality assessments in wine making. 

- The Python script titled 'WineQT2.py' addresses the problem by analyzing the Wine Quality dataset to compare the typical chemical profiles of high-quality wines (rated 7 or above) against standard wines (rated 5-6). It solves the problem by loading the CSV data with pandas, filtering the dataset into the two quality categories, and computing mean values for key physiochemical features like alcohol, volatile acidity, and sulphates. The results are presented in a concise comparison table, highlighting differences that reveal patterns—such as higher alcohol and lower volatile acidity in premium wines.

<img width="1200" height="800" alt="Physicochemical profiles comparison" src="https://github.com/user-attachments/assets/e3e7c09f-22e7-48b8-9009-7824f784d383" />

- Using pandas, we compute the distributions and visualized trends for the red wine dataset to guide inventory managament and marketing. The 'quality' column rates wines on a scale from 3 (lowest) to 9 (highest), based on sensory data. The distribution is highly imbalanced, with the vast majority of wines falling into the average quality range (5 and 6), reflecting real-world wine production where "good enough" wines dominate.The python code is titled 'WineQT3'.

<img width="511" height="133" alt="Quality Distribution Table" src="https://github.com/user-attachments/assets/63a40a9b-6f2c-47ba-9397-c71187c5e35a" />

The distribution of the wine quality is shown in  the figure below:   
<img width="800" height="500" alt="Wine Quality Distribution" src="https://github.com/user-attachments/assets/c79b208e-9c4d-4461-902b-fee506f852c9" />

### Chemical Drivers of Vinho Verde Wine Quality
Analysis of the dataset highlights several chemical properties that strongly influence wine quality scores:
- Volatile Acidity (VA): This is the primary negative factor. Wines with VA above 0.6 g/L often develop acetic spoilage and vinegar-like off-flavors, contributing to lower quality scores. It should be noted that reducing VA through careful microbial control and fermentation management is essential.

- Alcohol: This is the main positive driver. Wines with alcohol content ≥12% ABV demonstrate improved body, mouthfeel, and fruit intensity, with most top-scoring wines falling into this range. Controlled fermentation can strategically enhance these characteristics.

- Sulphates: Support quality by improving freshness and providing antimicrobial stability, with optimal levels between 0.6–0.8 g/L.

Additional contributors: Citric acid and fixed acidity enhance freshness and structure, while excessive sulfur dioxide can slightly detract from quality.

Implications for Production:
Adjusting fermentation conditions, controlling microbial activity, and balancing alcohol and sulphates are actionable levers to improve wine quality from standard to high-scoring profiles.

### High vs Standard Wines
High-quality wines consistently show elevated levels of desirable compounds (e.g., alcohol, sulphates, citric acid) that contribute to enhanced flavor complexity, body, and freshness, while exhibiting reduced concentrations of potential detractors (e.g., volatile acidity, total sulfur dioxide). This aligns with sensory science principles, where balanced acidity and alcohol amplify mouthfeel and aroma persistence, as supported by expert ratings in the dataset. The profiles show that minor optimisations, rather than extreme values, drive quality; for example, a 15% rise in alcohol and a 19% reduction in volatile acidity account for a large portion of the variation.  Consistent patterns confirm these as quality indicators, although variability within groups (e.g., SD for alcohol: 0.85 in high vs. 0.92 in standard) implies environmental factors like vintage have a role.

### Implications of Wine Quality Distribution
A clear skewed distribution which highlights a concentration of average-rated wines (scores 5-6), dominating 86.53% of samples, which may reflect typical commercial production standards or rater biases toward mediocrity. Rare low scores (3-4, <5%) suggest minimal flawed batches, while underrepresented highs (7-8, ~9%) indicate exceptional vintages are outliers, challenging predictive models to handle class imbalance effectively.
Major implications of this distribution include:
- Imbalance in Quality Scores: The heavy concentration in qualities 5 and 6 suggests that the dataset reflects a production-focused inventory where "good but not exceptional" wines dominate. This could stem from factors like grape sourcing or fermentation consistency, leading to predictable mid-tier outcomes. The rarity of extremes (very poor or excellent) indicates quality control measures that filter out outliers, but it also highlights potential stagnation in innovation—e.g., few high-alcohol or low-pH variants that might push scores higher.
- Implications for Business Operations: In inventory management, this distribution signals over-reliance on volume-driven mid-quality wines, which may yield steady but low-margin sales. For marketing, it underscores a challenge: differentiating products in a saturated "average" segment could dilute brand perception, while the scarcity of premium (7+) wines limits upselling opportunities. Statistically, the mean quality is approximately 5.6, reinforcing the "mediocre majority" trend. If this mirrors the full dataset, it implies  about 80-90% of stock is commoditized, vulnerable to price competition.

### Production Process Optimisation
- Prioritise reducing volatile acidity by strict sanitation, temperature-controlled fermentation (18–25°C), and early SO₂ dosage (20–50 mg/L) to maintain levels <0.5 g/L in order to maximise these effects, which might raise average quality by 0.5–1 point.
- Increase alcohol content without going overboard by using riper harvests (Brix 24–26°) and tolerant yeasts that target 12–14% ABV.  Aim for 10–15% quality increases every vintage in accordance with EU rules (total SO₂ <150 mg/L). Adjust sulphates to 0.6–1.0 g/L by precise additions and blending, monitored by titration, while using sensory trials and data analytics for iterative improvement.

2. Winemakers should incorporate these data-driven strategies to use these profiles for production targets, which could increase high-quality yields by 10–20% through focused interventions:

<img width="489" height="459" alt="Psychicochemical profile recommendation" src="https://github.com/user-attachments/assets/408febe3-5240-43a3-bd4b-b6f156d8bd36" />

These recommendations prioritize cost-effective, scalable changes, with ROI from premium pricing (e.g., +25% for ≥7 scores) outweighing minor additive costs

**Inventory Optimization**:
- Prioritize Mid-Tier Stocking: Allocate 70-80% of inventory to qualities 5-6 for reliable turnover, using just-in-time ordering to minimize holding costs and forecast demand with simple models to avoid overstocking the 86% majority.
 
- Build Premium Reserves: Dedicate 10-15% of capacity to sourcing/acquiring more quality 7+ wines (e.g., via supplier partnerships for low-volume, high-acid varietals). Also, aim to increase their share to 15% within 6-12 months to balance the skew and hedge against mid-tier market saturation.
  
- Cull Low-Quality Outliers: Phase out qualities 3-4 (under 5% of stock) through discounts or blending into value packs, freeing shelf space and reducing waste.

**Marketing Strategies**:

- Segmented Campaigns: Market quality 5-6 wines as "everyday essentials" with bundle deals (e.g., "Buy 6, Save 20%") to drive volume. For 7+ wines, position as "collector's choice" with storytelling (e.g., "Handcrafted from rare vintages") and limited-edition releases to justify 20-50% price premiums.

- Data-Driven Personalization: Use the dataset insights to segment customers—e.g., via Python clustering (scikit-learn's KMeans on quality + alcohol) to target "value seekers" (qualities 5-6) with email promotions and "aspirational buyers" (7+) with exclusive tastings.

- Quality Enhancement Initiatives: Invest in R&D (e.g., experimenting with citric acid levels, as higher values correlate with better scores in similar datasets) to shift future distributions toward 6+ while tracking the progress with quarterly re-analysis of production data.

### Tools
- Excel (Data cleaning)
- Python (Panda - Data Aggregation, Matplot - Data Visualization)
- Power BI (Data Visualization)

### Data Sources
The primary dataset is sourced from the provided "WineQT.csv" file, derived from the UCI Wine Quality dataset. It includes 1143 records with the following columns:

- id: Sequential identifier
- fixed acidity: Tartaric acid (g/dm³)
- volatile acidity: Acetic acid (g/dm³)
- citric acid: Citric acid
- residual sugar: Sugar post-fermentation (g/dm³)
- chlorides: Sodium chloride (g/dm³)
- free sulfur dioxide: Free SO₂ (mg/dm³)
- total sulfur dioxide: Total SO₂ (mg/dm³)
- density: Density SO₂ (g/cm³)
- pH: Acidity level (0-14 scale)
- sulphates: Potassium sulphate (mg/dm³)
- alcohol: Alcohol content (% by volume)
- quality: Expert-rated score (3-8)

This dataset is pubicly available on Kaggle and UCI machine learning repository, https://archive.ics.uci.edu/ml/datasets/wine+quality
