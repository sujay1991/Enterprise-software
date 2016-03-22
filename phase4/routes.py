__author__ = 'pymavericks'
#import required libraries
from flask import *
import pymongo

#Establish database connection
connection = pymongo.MongoClient("mongodb://pymavericks:Nbeke44H@labs.ayokasystems.com/?authSource=pymavericks")

db = connection.pymavericks

app = Flask(__name__)

# create a list of all the keys in mongodb collections

indi_cols = ["primaryid","caseid","indi_drug_seq","indi_pt"]
drug_cols=["primaryid","caseid","drug_seq","role_cod","drugname","val_vbm","route","dose_vbm","cum_dose_chr","cum_dose_unit","dechal","rechal","lot_num","exp_dt","nda_num","dose_amt","dose_unit","dose_form","dose_freq"]
demo_cols=["primaryid","caseid","caseversion","i_f_code","event_dt","mfr_dt","init_fda_dt","fda_dt","rept_cod","mfr_num","mfr_sndr","age","age_cod","gndr_cod","e_sub","wt","wt_cod","rept_dt","to_mfr","occp_cod","reporter_country","occr_country"]
reac_cols=["primaryid","caseid","pt"]
ther_cols=["primaryid","caseid","dsg_drug_seq","start_dt","end_dt","dur","dur_cod"]
rxtermsArch_cols=["RXCUI","GENERIC_RXCUI","TTY","FULL_NAME","RXN_DOSE_FORM","FULL_GENERIC_NAME","BRAND_NAME","DISPLAY_NAME","ROUTE","NEW_DOSE_FORM","STRENGTH","SUPPRESS_FOR","DISPLAY_NAME_SYNONYM","IS_RETIRED","SXDG_RXCUI","SXDG_TTY","SXDG_NAME"]
rxterms_cols=["RXCUI","GENERIC_RXCUI","TTY","FULL_NAME","RXN_DOSE_FORM","FULL_GENERIC_NAME","BRAND_NAME","DISPLAY_NAME","ROUTE","NEW_DOSE_FORM","STRENGTH","SUPPRESS_FOR","DISPLAY_NAME_SYNONYM","IS_RETIRED","SXDG_RXCUI","SXDG_TTY","SXDG_NAME"]
outc_cols=["primaryid","caseid","outc_cod"]
rxing_cols=["RXCUI","INGREDIENT","ING_RXCUI"]
rspsr_cols=["primaryid","caseid","rpsr_cod"]
ndfrt_p_data_cols = ["Term", "Code"]
ndfrt_data_cols = ["DefType", "code", "id"]

final_data = {}

#Main page routing
@app.route("/")
def index():
    return render_template("search.html")

#Search Page routing
@app.route("/search",methods=["GET","POST"])
def searchhome():
    return render_template("search.html")

#Output page routing
@app.route("/output",methods=["GET","POST"])
def output():
    return render_template("output.html")

#Search Page with search term routing
@app.route("/search/find",methods=["GET","POST"])
def search():
    try:
        indi_quer={}
        indi_result = []
        vFound = False
        key=request.args.get("key")

        # query indi_data and build the resultset
        for col in indi_cols:
            indi_quer.update({col:key})
        for k,v in indi_quer.iteritems():
            res = {}
            if vFound == False:
                res = db.indi_data.find({k:{"$regex":v}})
                if res.count() > 0:
                    vFound = True
                for doc in res:
                    print type(doc)
                    indi_result.append(doc)
            #add the result to the final_data dictionary
            final_data.update({"indi_data":indi_result})


        # query drug_data and build the resultset
        drug_quer={}
        drug_result=[]
        vFound = False
        for col in drug_cols:
            drug_quer.update({col:key})
        for k,v in drug_quer.iteritems():
            res = {}
            if vFound ==False:
                res = db.drug_data.find({k:{"$regex":v}})
                if res.count() > 0:
                    vFound = True
                for doc in res:
                    drug_result.append(doc)
            #add the result to the final_data dictionary
            final_data.update({"drug_data":drug_result})


        # query demo_data and build the resultset
        demo_quer={}
        demo_result=[]
        vFound = False
        for col in demo_cols:
            demo_quer.update({col:key})
        for k,v in demo_quer.iteritems():
            res = {}
            if vFound == False:
                res = db.demo_data.find({k:{"$regex":v}})
                if res.count() > 0:
                    vFound = True
                for doc in res:
                    demo_result.append(doc)
            #add the result to the final_data dictionary
            final_data.update({"demo":demo_result})


        # query reac_data and build the resultset
        reac_quer={}
        reac_result=[]
        vFound = False
        for col in reac_cols:
            reac_quer.update({col:key})
        for k,v in reac_quer.iteritems():
            res = {}
            if vFound == False:
                res = db.reac_data.find({k:{"$regex":v}})
                if res.count() > 0:
                    vFound = True
                for doc in res:
                    reac_result.append(doc)
            #add the result to the final_data dictionary
            final_data.update({"reac":reac_result})


        # query ther_data and build the resultset
        ther_quer={}
        ther_result=[]
        vFound = False
        for col in ther_cols:
            ther_quer.update({col:key})
        for k,v in ther_quer.iteritems():
            res = {}
            if vFound == False:
                res = db.ther_data.find({k:{"$regex":v}})
                if res.count() > 0:
                    vFound = True
                for doc in res:
                    ther_result.append(doc)
            #add the result to the final_data dictionary
            final_data.update({"ther_data":ther_result})

        # query rxarch_data and build the resultset
        rxtermsArch_quer={}
        rxtermsArch_result=[]
        vFound = False

        for col in reac_cols:
            rxtermsArch_quer.update({col:key})
        for k,v in rxtermsArch_quer.iteritems():
            res = {}
            if vFound == False:
                res = db.rxarch_data.find({k:{"$regex":v}})
                if res.count() > 0:
                    vFound = True
                for doc in res:
                    rxtermsArch_result.append(doc)
            #add the result to the final_data dictionary
            final_data.update({"rxtermsArch_data":rxtermsArch_result})

        # query rxterms_data and build the resultset
        rxterms_quer={}
        rxterms_result=[]
        vFound = False
        for col in reac_cols:
            rxterms_quer.update({col:key})
        for k,v in rxterms_quer.iteritems():
            res = {}
            if vFound == False:
                res = db.rxterms_data.find({k:{"$regex":v}})
                if res.count() > 0:
                    vFound = True
                for doc in res:
                    rxterms_result.append(doc)
            #add the result to the final_data dictionary
            final_data.update({"rxterms_data":rxterms_result})

        # query outc_data and build the resultset
        outc_quer={}
        outc_result=[]
        vFound = False

        for col in outc_cols:
            outc_quer.update({col:key})
        for k,v in outc_quer.iteritems():
            res = {}
            if vFound == False:
                res = db.outc_data.find({k:{"regex":v}})
                if res.count() > 0:
                    vFound = True
                for doc in res:
                    outc_result.append(doc)
            #add the result to the final_data dictionary
            final_data.update({"outc_data":outc_result})

        # query rxing_data and build the resultset
        rxing_quer={}
        rxing_result=[]
        vFound = False

        for col in rxing_cols:
            rxing_quer.update({col:key})
        for k,v in rxing_quer.iteritems():
            res = {}
            if vFound == False:
                res = db.rxingr_data.find({k:{"$regex":v}})
                if res.count() > 0 :
                    vFound = True
                for doc in res:
                    rxing_result.append(doc)
            #add the result to the final_data dictionary
            final_data.update({"rxing":rxing_result})

        # query rspsr_data and build the resultset
        rspsr_quer={}
        rspsr_result=[]
        vFound = False
        for col in rspsr_cols:
            rspsr_quer.update({col:key})
        for k,v in rspsr_quer.iteritems():
            res = {}
            if vFound == False:
                res = db.rspsr_data.find({k:{"$regex":v}})
                if res.count() > 0:
                    vFound = True
                for doc in res:
                    rspsr_result.append(doc)

            #add the result to the final_data dictionary
            final_data.update({"rspsr":rspsr_result})

        # query ndfrt_p_data and build the resultset

        ndfrt_p_data_quer = {}
        ndfrt_p_data_result = []
        vFound = False

        for col in ndfrt_p_data_cols:
            ndfrt_p_data_quer.update({col:key})
        for k,v in  ndfrt_p_data_quer.iteritems():
            res = {}
            if vFound == False:
                res = db.ndfrt_p_data.find({k:{"$regex":v}})
                if res.count() > 0:
                    vFound = True
                for doc in res:
                    ndfrt_p_data_result.append(doc)

            #add the result to the final_data dictionary
            final_data.update({"ndfrt_p_data":ndfrt_p_data_result})

        # query ndfrt_data and build the resultset
        ndfrt_data_quer = {}
        ndfrt_data_result = []
        vFound = False

        for col in ndfrt_data_cols:
            ndfrt_data_quer.update({col:key})
        for k,v in ndfrt_data_quer.iteritems():
            res = {}
            if vFound == False:
                res = db.ndfrt_data.find({k:{"$regex":v}})
                if res.count() > 0 :
                    vFound = True
                for doc in res:
                    ndfrt_data_result.append(doc)

            #add the result to the final_data dictionary
            final_data.update({"ndfrt_data":ndfrt_data_result})

        return render_template("output.html",data=final_data)
    except:
        return render_template("error.html")

@app.errorhandler(404)
def page_not_found(e):
    return render_template('error.html'), 404

if __name__ == "__main__":
    app.run(debug = True)



