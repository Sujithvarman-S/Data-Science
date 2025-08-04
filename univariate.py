class univariate():
    
    def QualQuan(dataset): # if you mentioned any variable in open paranthisis only, you can use the class in future...
    
        Qual=[]
        Quan=[]
        
        for columnName in dataset.columns:
            
            if(dataset[columnName].dtypes=="O"):
                #print("Qual")
                Qual.append(columnName)                ##### Function created #####
                
                
            else:                              
                #print("Quan")
                Quan.append(columnName)
                
        return Qual,Quan
        

    

    def freq_table(dataset, columnName):  # upgraded frequency_table is in "TSA"(descriptive.py),refer if you need...
    
        freq_table=pd.DataFrame(columns=["unique_values","frequency","relative_frequency","cummulative_relative_frequency"])
        
        freq_table["unique_values"]= dataset[columnName].value_counts().index
        freq_table["frequency"]= dataset[columnName].value_counts().values
        freq_table["relative_frequency"]= freq_table["frequency"]/103        # 103 indicates total number of column......
        freq_table["cummulative_relative_frequency"]= freq_table["relative_frequency"].cumsum()
                                                        # cumsum is a inbuilt feature for finding cumulative relative frequency..
        return freq_table
        


    def univariate(dataset,Quan):
    
    
        descriptive = pd.DataFrame(index= 
        ["mean","median","mode","Q1:25%","Q2:50%","Q3:75%","Q4:100%","IQR","1.5_Rule","lesser_outlier","higher_outlier","min","max"],columns=Quan)
        for columnName in Quan:
            descriptive[columnName]["mean"]=dataset[columnName].mean()
            descriptive[columnName]["median"]=dataset[columnName].median()
            descriptive[columnName]["mode"]=dataset[columnName].mode()[0]
            
            #descriptive[columnName]["Q1:25%"]=np.percentile(dataset[columnName],25) #it will ouptput with error(NAN) because the dataset is not preproccesed,so
            descriptive[columnName]["Q1:25%"]= dataset.describe()[columnName]["25%"]
            descriptive[columnName]["Q2:50%"]= dataset.describe()[columnName]["50%"]
            descriptive[columnName]["Q3:75%"]= dataset.describe()[columnName]["75%"]
            descriptive[columnName]["Q4:100%"]= dataset.describe()[columnName]["max"]
            descriptive[columnName]["IQR"]= descriptive[columnName]["Q3:75%"] - descriptive[columnName]["Q1:25%"]
            descriptive[columnName]["1.5_Rule"]= 1.5* descriptive[columnName]["IQR"]
            descriptive[columnName]["lesser_outlier"]= descriptive[columnName]["Q1:25%"] - descriptive[columnName]["1.5_Rule"]
            descriptive[columnName]["higher_outlier"]= descriptive[columnName]["Q3:75%"] + descriptive[columnName]["1.5_Rule"]
            descriptive[columnName]["min"]= dataset[columnName].min()
            descriptive[columnName]["max"]= dataset[columnName].max()
            descriptive[columnName]["skewed"]=dataset[columnName].skew()
            descriptive[columnName]["kurtosis"]=dataset[columnName].kurtosis()
            descriptive[columnName]["variance"]=dataset[columnName].var()
            descriptive[columnName]["standard_deviation"]=dataset[columnName].std()
    
        
        return descriptive

    


    def outlier_finder(descriptive,Quan):
    
        lesser_outlier=[]
        higher_outlier=[]
                                        # checking and getting outlier column......
        for columnName in Quan:
            columnName
            if(descriptive[columnName]["min"] < descriptive[columnName]["lesser_outlier"]):
                lesser_outlier.append(columnName)
            if(descriptive[columnName]["max"] > descriptive[columnName]["higher_outlier"]):
                higher_outlier.append(columnName)
                
        return lesser_outlier,higher_outlier

    


    def get_pdf(dataset,startrange,endrange):

    
        from matplotlib import pyplot as plt
        from scipy.stats import norm as nor    # this library used for importing "Normal Distribution".....
        import seaborn as sns
        
        ax=sns.distplot(dataset,kde=True,kde_kws={"color":"blue"},color="Green")
        plt.axvline(startrange,color="Red")                  # creating skeleton for the distribution.....
        plt.axvline(endrange,color="Red")
        
        sample=dataset
        sample_mean=sample.mean()
        sample_std=sample.std()
        print("mean=%.3f,standard_deviation=%.3f" % (sample_mean,sample_std))  # creating "Normal Distribution" using mean and std...
        dist=nor(sample_mean,sample_std) 
        
        
        values=[value for value in range(startrange,endrange)]
        probabilities=[dist.pdf(value)for value in values]             # using "Normal Distribution" getting probability value of "pdf"....
        prob=sum(probabilities)
        print("the area between range({},{}:){}".format(startrange,endrange,prob))


    return prob



    def SND(dataset):
    
        import seaborn as sns
        
        mean=dataset.mean()
        std=dataset.std()
        
        values=[i for i in dataset]
        z_score = [((j-mean)/std) for j in values]
        
        sns.distplot(z_score,kde=True)
        