// JavaScript Document
function FillValues(frm)
{
	 //alert ("fgdfg");
	if (frm.chkFill.checked)
	{
		frm.delAddress.value		= frm.address.value;
		frm.delAddress3.value		= frm.address2.value;
		frm.txtDelCity.value		= frm.city.value;
		frm.txtDelCounty.value		= frm.state.value;
		frm.txtDelPostCode.value	= frm.zipcode.value;
		frm.txtDelPhone.value		= frm.phone.value;
		
	}
	else
	{
		frm.delAddress.value		= "";
		frm.delAddress3.value		= "";
		frm.txtDelCity.value		= "";
		frm.txtDelCounty.value		= "";
		frm.txtDelPostCode.value	= "";
		frm.txtDelPhone.value		= "";
	}	
		
}
function FillValues1(frm)
{
	 //alert ("fgdfg");
	if (frm.chkFillValues.checked)
	{
		frm.selAccTitle.value		= frm.SelTitle.value;
		frm.txtAccFirstName.value	= frm.firstName.value;
		frm.txtAccSurName.value		= frm.lastName.value;
		frm.txtAccEmail.value		= frm.email.value;
		frm.txtAccPhone.value		= frm.phone.value;
		frm.txtAccPostCode.value	= frm.txtCompFax.value;
	}
	else
	{
		frm.selAccTitle.value		= "";
		frm.txtAccFirstName.value	= "";
		frm.txtAccSurName.value		= "";
		frm.txtAccEmail.value		= "";
		frm.txtAccPhone.value		= "";
		frm.txtAccPostCode.value	= "";
	}	
		
}


