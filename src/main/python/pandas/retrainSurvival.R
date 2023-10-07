library("survival")
library("survminer")
library("caret")



data <- read.csv(file = 'data/Hackathon Challenge 2 Data Set.csv')
head(data)

cols <- colnames(data) 


# Uni-variate Cox regression
#retain.cox1 <- coxph(Surv(Length.of.Service, RETAINED) ~ INTERVENTION, data=data)
#retain.cox1


dummy <- dummyVars(" ~ .", data=data)
newdata <- data.frame(predict(dummy, newdata = data)) 
head(newdata)
newCols <- colnames(newdata) 

oneHotcols <- newCols[which(!newCols %in% cols)]

paste(pred_df$predictors, collapse = " + ")

# Multi-variate Survival
retain.cox2 <- coxph(Surv(Length.of.Service, RETAINED) ~ INTERVENTION + Ratio.Category + Category.1 + Last.Change.Category + Time.In.Role.Category + 
                       Org.Unit. + Org.Unit.Business_01 + Org.Unit.Business_02 + Org.Unit.Business_03 + Org.Unit.Business_04 + Org.Unit.Business_05 + Org.Unit.Client_01 + Org.Unit.Client_02 + Org.Unit.Client_03 + Org.Unit.Enabling_01 + Org.Unit.Enabling_02 + Org.Unit.Enabling_03 + Org.Unit.Support_01 + Org.Unit.Support_02 + Org.Unit.Technical_01 + Org.Unit.Technical_02 + Org.Unit.Technical_03 + Organization. + Organization.Analytics_01 + Organization.Client_01 + Organization.Client_02 + Organization.Consulting_01 + Organization.Consulting_02 + Organization.Consulting_03 + Organization.Development_01 + Organization.Development_02 + Organization.Development_03 + Organization.Development_04 + Organization.Development_05 + Organization.Development_06 + Organization.Development_07 + Organization.Development_08 + Organization.Development_09 + Organization.Development_10 + Organization.Development_11 + Organization.Development_12 + Organization.Development_13 + Organization.Enabling_01 + Organization.Enabling_02 + Organization.Enabling_03 + Organization.Enabling_04 + Organization.Healthcare_01 + Organization.Healthcare_02 + Organization.Healthcare_03 + Organization.Healthcare_04 + Organization.Healthcare_05 + Organization.International_01 + Organization.IT_01 + Organization.IT_02 + Organization.IT_03 + Organization.IT_04 + Organization.IT_05 + Organization.IT_06 + Organization.IT_07 + Organization.IT_08 + Organization.Operations_01 + Organization.Operations_02 + Organization.Other + Organization.Product_01 + Organization.Product_02 + Organization.Product_03 + Organization.Product_04 + Organization.Professional.Services_01 + Organization.Professional.Services_05 + Organization.Sales_01 + Organization.Sales_02 + Organization.Sales_03 + Organization.Support_01 + Organization.Support_02 + Organization.Support_03 + Organization.Support_04 + Organization.Support_05 + Job.Family.Group. + Job.Family.Group.Business.Development...Sales + Job.Family.Group.Client.Relationships + Job.Family.Group.Consulting.Services + Job.Family.Group.Corporate.Administration...Facilities + Job.Family.Group.Data.Analytics...Business.Intelligence + Job.Family.Group.Development + Job.Family.Group.Finance + Job.Family.Group.General.Business.Management + Job.Family.Group.Health...Care.Services + Job.Family.Group.Human.Resources + Job.Family.Group.Information.Technology + Job.Family.Group.Legal..Compliance...Audit + Job.Family.Group.Marketing..Communications...Corporate.Affairs + Job.Family.Group.Product.Management...Planning + Job.Family.Group.Project...Program.Management + Job.Family.Group.Support.Services...Operations + Direct.Reports.Category. + Direct.Reports.Category.High + Direct.Reports.Category.Low + Direct.Reports.Category.Medium + Direct.Reports.Category.None + Direct.Reports.Category.Very.High + Span.of.Control.Category. + Span.of.Control.Category.High + Span.of.Control.Category.Higher + Span.of.Control.Category.Low + Span.of.Control.Category.Medium + Span.of.Control.Category.None + Location.1. + Location.1.Location_01 + Location.1.Location_02 + Location.1.Location_03 + Location.1.Location_04 + Location.1.Location_05 + Location.1.Location_06 + Work.Country. + Work.Country.Country_01 + Work.Country.Country_02 + Work.Country.Country_03 + Work.Country.Country_04 + Work.Country.Country_05 + Work.Country.Country_06 + Work.Country.Country_07 + Work.Country.Country_08 + Work.Country.Other, data=newdata)
summary(retain.cox2)


plot(survfit(retain.cox2, data=newdata))




retain.cox3 <- coxph(Surv(Length.of.Service, RETAINED) ~  INTERVENTION + Ratio.Category + Category.1 +  Last.Change.Category + 
                       Organization.Development_02 + Organization.IT_02 + Organization.IT_05  + Organization.IT_06 + Organization.Support_04 + 
                       Job.Family.Group.Consulting.Services + Work.Country.Country_04, data=newdata)
summary(retain.cox3)

ggsurvplot(survfit(retain.cox3, data=newdata), palette = "#2E9FDF", ggtheme = theme_minimal())




