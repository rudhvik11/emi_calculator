import streamlit as st
st.title("IMPROVISED E.M.I  CALCULATOR")
p = st.slider("Principle",1000,10000000)
n = st.slider("Tenure(in months)",1,120)
r = st.slider("R.O.I",0.01,15.00)
m = st.slider("Period after which the Outstanding Loan Balance is calculated (in months)",1,60)
n = n*12
r = r/12
m = 1 - (n*12)

@st.cache()
def calculate_emi(Principle,Tenure,roi) :
	emi = (p*r/100*(1 + r/100)**n/((1 + r/100)**n - 1))
	return emi

def calculate_outstanding_balance(Principle,Tenure,roi,outstanding_balance) :
	balance = (p*(1 + r/100)**n - (1 + r/100)**m) / ((1 + r/100)**n - 1)
	return balance

if st.button("calculate EMI") :
	result = calculate_emi(p,n,r)
	amount = round(result,3)
	st.write("the emi is ", amount)

if st.button("calculate outstanding balance") :
	result_1 = calculate_outstanding_balance(p,n,r,m)
	amount_1 = round(result_1,3)
	st.write("the outstanding loan balance is ",amount_1)