# Chapter 1: Structural Transformation and Foreign Direct Investment

## Structural transformation and FDI?

  - China attracted foreign direct investment (FDI) more than any other developping countries
    - the literature mentions the agglomeration effect to explain multinational activities abroad
    - Market Structure
  - Meanwhile, China shifted its production of goods formerly produced by low-income countries to those comparable in rich countries (McMillan et al. 2014)
    - The litterature explained product upgrading through the transfer of resources from low productivity into activities with high productivity

  - The value added of this paper is to link both literature: FDI and Structural transformation

## Product Upgrading

  - Definition of product upgrading: the ability of a country to build and diversify its stock of ‘*capabilities*’ to produce complex goods.

  - Learn more about capabilities [here for graphics](https://atlas.media.mit.edu/en/visualize/network/hs92/export/chn/all/show/2017/) and [here for computation](https://dynalist.io/d/o8RPy5asVhNW70rVLysTKo4t)

  Evolution of Economic Complexity of China over time

  <img src="https://github.com/thomaspernet/research-phd/raw/master/img/1.png" >

  Mapping of product space of China: The product space is a network connecting products that are likely to be co-exported and can be used to predict the evolution of a country’s export structure.

  <img src="https://github.com/thomaspernet/research-phd/raw/master/img/2.png">

## Why is it interesting?

### 4 contributions to the literature

  - The litterature on Structural Transformation investigates the impact on economic growth and on export growth

    - Poncet and Waldemar (2013) found that Chinese cities specializing in complex goods geared towards high productivity have a larger level of growth

  - Extend current model of location choice with a new indicator of capabilities

    - Location choice model : decision to invest at the firm level in a large number of possible region
    - Use of city-industry specific index to capture the structural transformation
      - Product upgrading is captured by a new indicator that empirically reveals the level of knowledge through the theory of capabilities

  - Provide response to empirical difficulties to measure local economic environment

    - Data on local economic environment covers a finer level of disaggregation both in term of geography of investment and sector of activities
    - Role of capabilities is specific to sector and city
    - The endogeneity problem has been addressed by including similar control variables in the literature and fixed effects in the baseline equation.

  - Role of processing trade

    - Processing trade is one of the most popular trade policies in China that aims to import tariff-free intermediate goods with high technological content while exporting goods to be sold to third-party countries
    - This policy intends to promote product quality upgrading through domestic firms’ progressive research and technology transfer.
      - technology transfer does not take place for firms operating in the processing trade
      - confine FDI and assembly activities in areas dedicated for this purpose, leading to a disconnection between the domestic producer and the foreign firm.
    - these are the ‘upstream-downstream’ links (purchase of intermediate input from a foreign firm and sale of the processed product to a domestic buyer) which generate technology transfer

## Findings

### Role of productive structure on FDI inflow 

(more [information](https://dynalist.io/d/o8RPy5asVhNW70rVLysTKo4t) about the strategy)

  - Region that have succeeded to build sophisticated industries enjoy larger amount of FDI
  - Complexity is stable at .29, significant at 1 percent across all column 
    - marginal impact : a 10% increase in complexity leads to 30% increase of the likelihood for an average investor
  - Agglomeration effect are found positive, very significant and same order of magnitude as in the literature
  - Firms have strong incentive to invest in city with favorable industrial policy

<img src="https://dynalist.io/u/wFzZwD65NnC27KzONC23D3Ye" >

### Sector specific

  - Target processing trade sector has no effect on FDI
  - Target innovative sectors is fundamental to bring more FDI

<img src="https://dynalist.io/u/QrsHiikuoebZ78lBEZlXpqJC" >

# Economic Openness, Industrial Policies and Quality Upgrading: Evidence from China

  - Achieving economic development requires a change in the industrial structure. 
    - Countries must begin to reallocate resources to products with more **significant potential** and intrinsic features that do not restrict the capacity to innovate
    - Need of diversification
  - The government must guide the transformation by opting for industrial policies that promote continuous product upgrading
  - The determinants of structural transformation and quality upgrading through an original inudstrial policy: The Chinese VAT rebate system

## Quality

### Quality and firm performance

  - Firms exporting high-quality (price) products have high revenue, access a large number of destination markets and pay high wages 
  - first models attempt to explain the selection of firms in the export market through productivity
    - only the most productive companies will be able to export goods with a lower unit cost
  - More recent models assumes that the consumer is more sensitive to the quality-adjusted price than the observed price
  - This quality parameter represents a shift in demand. 
    - Companies compete not only with prices but also with horizontal differentiation.
  - These models explain the extent to which firms can cope with the fixed cost of exporting by charging higher prices in more distant and more competitive countries.


### Quality and Tariff

  - Following a trade liberalization, firm purchase higher quality input to enter more profitable market
    - Improve quality to escape competition

  - More about the computation of quality can be found [here](https://dynalist.io/d/hnOnutKtJdI6IPjlF_IrsBQi)

## Industrial policy

  - Good policy foster export: VAT rebate is a tool to keep export values high

## VAT tax in China

### Main Objectives

  - VAT rebate policy, initiated by the State administration of Taxation, is designed to achieve 2 main objectives.

    - Reallocation to reduce trade dispute
    - Promote high quality products such as aviation and medical product and reduce export of polluting activities.

  - The Chinese export VAT refund mechanism in practice does not allow full recovery of the input VAT incurred for raw materials or components imported or purchased locally

    - There are 5 ranks from 5% to 17% and Chinese government frequently changes the rate according to the goals pursued
      - For example, a product with a 17 percent VAT rate and a 13 percent discount rate means 4 percent tax for the exporting company
    - The amount of VAT payable is based on the quantity exported.

### Eligibility rule for VAT rebate

  - processing trade with supplied materials are disqualified from the rebates.
  - The typical export VAT policy is that of “exempt, credit, and refund” (or “refund after collection”)
  - the “no collection and no refund” policy applies to processing trade with supplied inputs.
  - Even if the exporter pays VAT on local purchases, there is no entitlement to any export refund.
  - Expect VAT rebates to only have an effect on eligible export activities (ordinary and processing trade with imported materials)


## Identification Strategy

- Recent works on the export data for firms have shown the enormous gains from quality upgrading.
- We investigate first the impact of a change in the export tax on the product upgrading for a panel of Chinese domestic firms.

### Difference-in-difference

- More about the strategy can be found [here](https://dynalist.io/d/hnOnutKtJdI6IPjlF_IrsBQi)

  - The dependent variable is an indicator of quality measured for the firm’product’year.
  - Exploits both the variation in VAT rebate and the existence of a control group composed of processing firms with similar export characteristics as ordinary firms

    - require that for each ordinary firm there is at least one processing firm exporting the same product to the same destination in the same year.
    - analysis focuses on domestic Chinese ordinary and processing firms by excluding foreign-owned companies.

  $$Quality_{ikcdt} = \beta_{1}Ordinary^{E}_{i}*\text{Ln VAT export tax}_{k, t-1}+\beta_{5} Ordinary_{i}^{E}*\text{Ln import tax}_{k, t-1}+ \delta Competition_{s, t 1}+\beta_{4}Size_{i,t0}^{E}*\alpha_{t}+\alpha_{ik}+\alpha_{ct}+\alpha_{dt}+\alpha_{st}^{E}+ \epsilon_{ikcdt} $$

### Include several fixed effect

  - for sectorial, destination (origin) and location time-varying shocks which may affect firms' prices.
  - Some unobservable shocks (e.g.,specific policies at the sectorial–regional level).=> control group of processing firms => affect prices of ordinary and processing firms similarly.

### Endogeneity

  - potential endogeneity between tariff changes and the quality of firms.

    - firms' processing status is exogenous to the level of VAT rebate
    - control group is similar to our treated group in terms of ownership and export patterns by
      - (i) excluding foreign-owned companies
      - (ii) requiring that, for each ordinary firm, there is at least one processing firm exporting the same HS6 product to the same destination in the same year

## Results

- difference-in-difference estimation
  - Processing traders constitute the control group, because they cannot be eligible for VAT reimbursement
  - control for unobservable variables that do not vary over time and any other shock affecting the origin/destination of exports.
- The role of VAT on quality
  - An increase in VAT tax has a negative impact on the quality of domestic ordinary trade firms.
  - Processing firms do not seem to be affected by the policy. 
  - Our regression reports that a 1  percentage point increase raises product upgrading by 1.5 percent. 

  <img src="https://dynalist.io/u/8MXZXv4tRhIbD-5lC62b4NjV" >
    
- Characteristics of  the destination countries, products, and companies
  - each regression controls for various fixed effects:
    -  size of firms, importing  countries, and origin of exports, but it also captures variations across firms and sectors.
  - When the government decides to raise the VAT rebates, the product improvement remains specific to exports to developed countries
  - products with a broad scope of differentiation will benefit  more from VAT rebates than homogeneous products (Rauch 1999 classification)
    - The tax does not uniformly affect all products and that policy makers should pay close attention to the type of goods targeted. 
  - Small firms may have less incentive to improve the quality than larger firms.

<img src="https://dynalist.io/u/EFGL1qVfFO6w2wDB2oH-nlaw" >

- More results can be found [here](https://dynalist.io/d/hnOnutKtJdI6IPjlF_IrsBQi)

# Product Upgrading And Pollution

### Facts

### Trade in China

  - China rapidly grow into the factory of the World, exporting goods and manuctured products everywhere in the world.

  - In 2005, the Chinese economy dethroned the US in the merchandised exported. Since then, China never stopped to increase the gap with the other economies

    <iframe width="600" height="400" src="https://datastudio.google.com/embed/reporting/1tMowiEW1NbF3L_5PjF7cfQoY-vEcRV1I/page/p5hh" frameborder="0" style="border:0" allowfullscreen></iframe>

### Pollution in China

  - China is a first class player in the world economy for the trade, growth, technology but China is also notorious for being a major polluter.
  
  - There is no other country in the world with a sharp increase as China.

    <iframe width="600" height="400" src="https://datastudio.google.com/embed/reporting/1tMowiEW1NbF3L_5PjF7cfQoY-vEcRV1I/page/Tohh" frameborder="0" style="border:0" allowfullscreen></iframe>

### Trade and Pollution

  - A closer look between the emission of SO3 and the merchandirse exported by China despicted a clear positive correlation.

  - The pollution in China is driven by the amount of merchandise exported to the rest of the world

    <iframe width="600" height="400" src="https://datastudio.google.com/embed/reporting/1tMowiEW1NbF3L_5PjF7cfQoY-vEcRV1I/page/x8hh" frameborder="0" style="border:0" allowfullscreen></iframe>

### Trade type, Quality and SO3

  - The chinese economy is stressing an export-oriented growth model, with a predominance for processing activities.

  - This economic system were relevant at the begining of the development stage but quickly reaches its limit.

  - The leaders of China are fully aware that significant progress has to be achieved in the need for quality growth

  - Xi Jinping launched a series of reforms to improve the lack of coordination and a more inclusive, green, innovation-driven growth and pollution free industries.

  - In this paper, we propose to establish a link between the quality enhancement of the Chinese economy and its impact on the environment.

    <iframe width="600" height="400" src="https://datastudio.google.com/embed/reporting/1tMowiEW1NbF3L_5PjF7cfQoY-vEcRV1I/page/rLJk" frameborder="0" style="border:0" allowfullscreen></iframe>

### Share of Trade type

  - Processing trade emits less pollution compared with ordinary trade. 
  - The share of processing is decreasing over time
    - Impact on the pollution emission? 

  <iframe width="600" height="400" src="https://datastudio.google.com/embed/reporting/1tMowiEW1NbF3L_5PjF7cfQoY-vEcRV1I/page/C2Lk" frameborder="0" style="border:0" allowfullscreen></iframe>

## What is the paper about?

  - The objective of the current paper is to show, ordinary trade is beneficial for the environment

    - Does structural transformation has a positive impact on the environment?

  - Adjustment mechanism

    - output quality depends on input quality and also implies a fixed cost for quality adjustment. Assume that producing high-quality outputs requires high-quality inputs.
    - quality increase with an increase in fixed quality investment: effectiveness of RD

  - Explain the decrease in average pollution level

    - The average level of pollution decreases because of:

    - Productivity effect:

      Upgrade quality through better intermediate input and better production structure. two types of fixed cost:

      - quality upgrading in the environmental sector
      - Export
      - Firms that export quality upgraded have higher productivity, ability to move toward cleaner industry, import better quality input

    - Reallocation effect:

      low productive firms in ordinary trade have two options:

      - Self-section in the export market firms that can't pay the fixed cost to export the upgraded environmental quality products have two possibilities:
        - reallocate to processing than lower pollution
      - reallocate to ordinary polluting activity?
        - reallocate to ordinary then constant or increase pollution

  - *Proposition 1*. An increase of the quality of the ordinary firms induces a reduction in the pollution level

  - *Proposition 2*: The least productive firm in ordinary activity leave the market or switch to processing activity (less polluting) inducing a reduction in the pollution level

## Why is it interesting?

  - Chinese Trade: switch from low quality to middle-high quality
  - Chinese type of trade: Lower processing trade. Increase ordinary trade
  - Increase quality leads to more revenue and more growth.
    - But, Sandra's paper shows ordinary trade does not improve the environment, then a negative impact on growth. More about the paper [here](https://dynalist.io/d/D9qe5sUl-G39NS5L2di0mrIj)
    - The effect is ambiguous.
  - Add the quality into the model to explore the relationship between structural transformation, and the environment.
  - The theoretical model shows an ambiguous effect in the firm selection: average ordinary us processing what effect prevail?
  - Interesting for the policymaker because: give incentives to move away from processing AND want to fight pollution.
    - This paper can provide both theoretical and empirical explanation

## Methodology

  - Level of analysis: city, industry and year.
  - pollution = quality + quality x status.
  - use the SO2 emission to compute the level of pollution at the industry level:
    - Environmentally extended input-output of China.
    - quality is computed using price index and “Khandelwal index.

## Test 

<iframe width="600" height="400" src="https://econ-complexity.herokuapp.com/"></iframe>