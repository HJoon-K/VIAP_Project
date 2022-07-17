function getCookie(name) {
	let cookieValue = null;
	if (document.cookie && document.cookie !== '') {
		const cookies = document.cookie.split(';');
		for (let i = 0; i < cookies.length; i++) {
			const cookie = cookies[i].trim();
			// Does this cookie string begin with the name we want?
			if (cookie.substring(0, name.length + 1) === (name + '=')) {
				cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
				break;
			}
		}
	}
	return cookieValue;
}  // crsf_token 쿠키

function Log(logStr) {
	console.log(logStr);
}

function numberMaxLength(e){
    if(e.value.length > e.maxLength){
        e.value = e.value.slice(0, e.maxLength);
    }
}		// number MaxLength

var emailCheckStatus = "y";  //n : 사용중 / y : 사용가능/ v : 올바르지 않은 이메일/ b : 입력하지 않음  
var carSizes = ["", "경형", "소형", "중형", "대형"];
var selDate = "";
var objPayPopup=null;
// ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
var agreeTerm = {
	termAllChk : function(){
		if(!$('#termAllChk').is(":checked")){ 
			$('.term').prop('checked', false).val("");
			$('.term').next('label').removeClass("selected");
		}else{
			$('.term').prop('checked', true).val("Y");
			$('.term').next('label').addClass("selected");
		}
		//noticeValue = $("#noticeChk").val();
		//alert (noticeValue);
	},
	termChk : function(id){
		if(!$('#'+id).is(":checked")){
			$('#'+id).val("");
			$('#'+id).next("label").removeClass("selected");
			
			$('#termAllChk').prop('checked', false).val("");
			$('#termAllChk').next('label').removeClass("selected");
		}else{
			$('#'+id).val("Y");
			$('#'+id).next("label").addClass("selected");
		}
		//noticeValue = $("#noticeChk").val();
		//alert (noticeValue);
	},
	testInfoChk : function(){
		if(!$('#myonoffswitch').is(":checked")){ 
			if($('#h_ttype').val() !='') {
				if(confirm("검사기초 정보가 있습니다.\n\n동의를 해제할 경우 기존 정보가 초기화 됩니다.\n\n진행 하시겠습니까?")) {
					$('.mk').prop('checked', false).val("");
					$('.mk').next('label').removeClass("selected");
					//기존 검사정보 초기화
					carInfo.initTestInfo();
				}
			//} else {
			//	$('.mk').prop('checked', false).val("");
			//	$('.mk').next('label').removeClass("selected");
			}
		//}else{
		//	$('.mk').prop('checked', true).val("Y");
		//	$('.mk').next('label').addClass("selected");
		}
	},
	openUserInfo : function(){
		window.scrollTo(0,0);
		$('#userInfoLayer').show();
	},
	closeUserInfo : function(){
		$('#userInfoLayer').hide();
		//약관확인 후 약관 위치로 이동
		var offset = $("#testagreement").offset();
		$('html, body').animate({scrollTop : offset.top-70}, 1200);
	},
	openPrivacyInfo : function(){
		window.scrollTo(0,0);
		$('#privacyInfoLayer').show();
	},
	closePrivacyInfo : function(){
		$('#privacyInfoLayer').hide();
		//약관확인 후 약관 위치로 이동
		var offset = $("#testagreement").offset();
		$('html, body').animate({scrollTop : offset.top-70}, 1200);
	},
	openNoticeInfo : function(){
		window.scrollTo(0,0);
		$('#noticeInfoLayer').show();
	},
	closeNoticeInfo : function(){
		$('#noticeInfoLayer').hide();
		//약관확인 후 약관 위치로 이동
		var offset = $("#testagreement").offset();
		$('html, body').animate({scrollTop : offset.top-70}, 1200);
	}
},

// ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
common = {
	ieCheckAgree : function(id){
		if($('#'+id).is(":checked")){
			$('#'+id).prop('checked', false).val("");
			$('#'+id).next("label").removeClass("selected");
		}else{
			$('#'+id).prop('checked', true).val("Y");
			$('#'+id).next("label").addClass("selected");
		}
	},
	propTrueCheck : function(selector){
		$(selector).prop('checked', true).val("Y");
		$(selector).next("label").addClass("selected");
	},
	propFalseCheck : function(selector){
		$(selector).prop('checked', false).val("");
		$(selector).next("label").removeClass("selected");
	}

},
// ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
AlertInfo = {
	validation : function(){

		if($('#sido').val() == '' || $('#gugun').val() == '' || $('#dong').val() == '') {
			alert(messages.do_alert_location);
			$('#sido').focus();
			return;
		}

		if($('#addretc').val() == '') {
			alert(messages.do_alert_addretc);
			$('#addretc').focus();
			return;
		}

		if($('#h_stype').val() == '1') {
			if($('#carname_alert').val() == '' || $('#expdate_alert').val() == '' || $('#alertdate').val() == '') {
				alert(messages.do_alert_test_info);
				$('#bymd').focus();
				return;
			}

			if($('#h_bymd').val() != $('#bymd').val()
				|| $('#h_carno').val() != $('#carno').val() ) {
				alert("[검사기초정보]\n조회한 정보가 다릅니다.");
				$('#bymd').focus();
				return;
			}
		}
		var carNo = $('#carno').val();
		 $("#carno").val(carNo.split(" ").join(""));

		if($('#carno').val() == '' ) {
			alert("차량번호를 입력해 주세요.");
			$('#carno').focus();
			return;
		}

		//자동차번호 형식 체크
		var checkNum = carInfo.checkCno($('#carno').val());
		if(checkNum != 1){
			alert("자동차번호 형식이 올바르지 않습니다.");
			$('#carno').focus();
			return;
		 }

		var name_alert = $("#name_alert").val();

		if( name_alert.length < 1 || name_alert.length > 20 ) {
			alert(messages.do_input_name);

			var offset = $("#register_alert").offset();
			$('html, body').animate({scrollTop : offset.top-70}, 1200);

			$('#name_alert').focus();
			return;
		}
		 $("#name_alert").val(name_alert.split(" ").join(""));
		name_alert = $("#name_alert").val();

		if(!checkEmoji(name_alert)) {
			alert(messages.do_name_guide);
			$('#name_alert').focus();
			return;
		 }

		if(!checkTel($("#tel1_alert").val(),'' ,'')) {
			alert(messages.do_alert_mobile_wrong + "\n" + messages.do_alert_mobile_wrong1);

			var offset = $("#register_alert").offset();
			$('html, body').animate({scrollTop : offset.top-70}, 1200);

			$('#tel1_alert').focus();
			return;
		}

	    if(emailCheckStatus != "y") {
			alert(messages.do_invalid_email);
			$('#email').focus();
			return;
		}

		if(!$('#alertChk').is(":checked")){
			alert(messages.do_agree_requirement_03);
			return ;
		}

		//$('#submitReqForm').submit();
		AlertInfo.alertSave();

	},
	alertSave : function() {

		$('#act').val('alert');

		$('#submitReqForm').ajaxForm({
			beforeSubmit: function (data,form,option) {
				return true;
			},
			url:"/data.html",
			success: function(data,status){
				if(data.result == "0000"){
					//대행 신청 완료
					var f = document.submitReqForm;
					f.target = '_self';
					f.method = 'post';
					f.enctype = "application/x-www-form-urlencoded";
					if($('#h_stype').val() == '1') {
						f.action = './p_test_alert_ok.html';
					}
					f.submit();
				}else{
					alert(data.message);
				}
			},
			error: function(){
				alert("오류발생 : 잠시후에 이용해 주시기 바랍니다.");
			}                               
		}).submit();
	},
	checkEmail : function() {
		emailCheckStatus = "y";
		/*
		var email = $("#email").val();

		if( email == "" ) {
			emailCheckStatus = "b";
			$("#email").val("");
			return;
		}

		var isValid = isValidEmail(email);
		if(isValid){
			emailCheckStatus = "y";
		}else{
			emailCheckStatus = "v";
		}
		*/
	}
},
// ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
personalAgentInfo = {
	validation : function(){

		if($('#sido').val() == '' || $('#gugun').val() == '' || $('#dong').val() == '') {
			alert(messages.do_alert_location);
			$('#sido').focus();
			return;
		}

		if($('#addretc').val() == '') {
			alert(messages.do_alert_addretc);
			$('#addretc').focus();
			return;
		}

		if($('#h_stype').val() == '1') {
			if($('#h_ttype').val() == '') {
				alert(messages.do_alert_test_info);
				$('#bymd').focus();
				return;
			}

			if($('#h_bymd').val() != $('#bymd').val()
				|| $('#h_carno').val() != $('#carno').val() ) {
				alert("[검사기초정보]\n조회한 정보가 다릅니다.");
				$('#bymd').focus();
				return;
			}
		}
		var carNo = $('#carno').val();
		 $("#carno").val(carNo.split(" ").join(""));

		if($('#carno').val() == '' ) {
			alert("차량번호를 입력해 주세요.");
			$('#carno').focus();
			return;
		}

		 //자동차번호 형식 체크
		 var checkNum = carInfo.checkCno($('#carno').val());
		 if(checkNum != 1){
			alert("자동차번호 형식이 올바르지 않습니다.");
			$('#carno').focus();
			return;
		 }

		if($('#schdate').val() == '' || $('#schtime').val() == '' || $('#h_cuno').val() == '' || $('#cuname').val() == '') {
			//검사희망일로 이동시키기 위해 한단계 위 엘리먼트 서비스이용료를 기준으로 잡음
			var offset = $("#totcost").offset();
		    $('html, body').animate({scrollTop : offset.top}, 400);

			alert('검사 희망일을 선택해주세요.');
			$('#schdate').focus();
			return;
		}
		var name = $("#name").val();

		if( name.length < 1 || name.length > 20 ) {
			alert(messages.do_input_name);

			var offset = $("#testuserinfo").offset();
			$('html, body').animate({scrollTop : offset.top-70}, 1200);

			$('#name').focus();
			return;
		}
		 $("#name").val(name.split(" ").join(""));
		 name = $("#name").val();

		 if(!checkEmoji(name)) {
			alert(messages.do_name_guide);
			$('#name').focus();
			return;
		 }

		if(!checkTel($("#tel1").val(),'' ,'')) {
			alert(messages.do_alert_mobile_wrong + "\n" + messages.do_alert_mobile_wrong1);

			var offset = $("#testuserinfo").offset();
			$('html, body').animate({scrollTop : offset.top-70}, 1200);

			$('#tel1').focus();
			return;
		}

	    if(emailCheckStatus != "y") {
			alert(messages.do_invalid_email);
			$('#email').focus();
			return;
		}

		if(!$('#userChk').is(":checked")){
			alert(messages.do_agree_requirement_01);
			return ;
		}else if(!$('#personalChk').is(":checked")){
			alert(messages.do_agree_requirement_02);
			return ;
		}

		if($('#p_method').val() == "1") {
			if(objPayPopup && !objPayPopup.closed) {
				//창이 있으면 닫는다.
				objPayPopup.self.close();
			} 
			objPayPopup = window.open('about:blank', 'payWindow', 'width=700, height=700');
		}

		//$('#submitReqForm').submit();
		personalAgentInfo.reservationSave();

	},
	reservationSave : function() {

		var p_method = $('#p_method').val();
		if(p_method == "0") {
			$('#act').val('req');
		} else {
			$('#act').val('check');
		}

		$('#submitReqForm').ajaxForm({
			beforeSubmit: function (data,form,option) {
				return true;
			},
			url:"/data.html",
			success: function(data,status){
				if(data.result == "0000"){
					//대행 신청 완료
					if(p_method == "1") {
						$('#h_ulist').val(data.ulist);
						var pf = document.frm;
						pf.GoodsName.value = data.gname;
						pf.Amt.value = data.amt;
						pf.Moid.value = data.moid;
						pf.MID.value = data.mid;
						pf.ReturnURL.value = data.rurl;
						pf.ResultYN.value = data.resultyn;
						pf.FORWARD.value = data.forward;
						pf.BuyerName.value = name;
						pf.BuyerTel.value = data.btel;
						pf.BuyerEmail.value = $('#email').val();
						pf.MerchantKey.value = data.mkey;
						pf.ediDate.value = data.edate;

						//$("#payButton").trigger("click");
						objPayPopup.location.href="pay.html";
						objPayPopup.focus();
					} else {
						var f = document.submitReqForm;
						f.target = '_self';
						f.method = 'post';
						f.enctype = "application/x-www-form-urlencoded";
						if($('#h_stype').val() == '1') {
							f.action = './p_test_req_ok.html';
						} else {
							f.action = './p_move_req_ok.html';
						}
						f.submit();
					}
				}else{
					alert(data.message);
				}
			},
			error: function(){
				alert("오류발생 : 잠시후에 이용해 주시기 바랍니다.");
			}                               
		}).submit();
	},
	checkEmail : function() {
		emailCheckStatus = "y";
		/*
		var email = $("#email").val();

		if( email == "" ) {
			emailCheckStatus = "b";
			$("#email").val("");
			return;
		}

		var isValid = isValidEmail(email);
		if(isValid){
			emailCheckStatus = "y";
		}else{
			emailCheckStatus = "v";
		}
		*/
	}
};

// ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
//$().ready(function() {
jQuery(document).ready( function(){
	//생년월일 등 숫자입력 폼에서 의도치 않은 스크롤로 인해 값이 변경되는 것을 막기 위해 스크롤 차단
	$(document).on("wheel", "input[type=number]", function (e) {
		$(this).blur();
	});





	$("#sido").on("click", function() {
		$('#btnCarLoc').trigger('click');
	});
	$("#locSido").on("change", function() {
		carInfo.loadAgentArea(2);
	});
	$("#locGugun").on("change", function() {
		carInfo.loadAgentArea(3);
	});
	$("#locDong").on("change", function() {
		carInfo.loadAgentArea(4);
	});

	$('.OpenChat').click(function(){
		$('.textLauncherIcon').trigger('click');
	});

	/*
	$("#input-12").fileinput({
		showPreview: false,
		allowedFileExtensions: ["jpg", "png", "jpeg", "gif"],
		elErrorContainer: "#errorBlock",
		mainClass: "input-group-lg",
		showUpload: true,
		maxFileCount: 5,
		previewFileType: "image",
		browseClass: "btn btn-success",
		browseLabel: "이미지 최대 5개",
		browseIcon: "<i class=\"icon-picture\"></i> ",
		removeClass: "btn btn-danger",
		removeLabel: "지우기",
		removeIcon: "<i class=\"icon-trash\"></i> ",
		uploadClass: "btn btn-info",
		uploadLabel: "업로드",
		uploadIcon: "<i class=\"icon-upload\"></i> "
	});
	*/
	// IE 인 경우 placeholder 미적용
	$('input:text').on("keyup", function() {
		if(isInternetExplorer() == "Y" ){
			common.checkIEForm($(this).attr("id"));
		}
	});

	$('#btnCpnApply').on("click", function() {
		if($('#totcost').val() =='') {
			alert('대행정보를 먼저 입력해주세요.');
			return false;
		}
		if($('#cpn').val() =='') {
			alert('쿠폰번호를 입력해주세요.');
			$('#cpn').focus();
			return false;
		}
		$('body').loading({
			stoppable: true,
			message: '쿠폰 확인중...',
			theme: 'dark'
		});
		//쿠폰처리를 위해 값을 넘길 때, 쿠폰적용지역 구분을 위해 시(도)정도도 함께 넘김
		$.ajax({
			type : "post",
			url : '/data.html?act=coupon',
			contentType : "application/x-www-form-urlencoded; charset=UTF-8",
			data : {"cpn" : $('#cpn').val(), "sido":$("#sido").val() },
			dataType : "json",
			success : function(data) {
				$('body').loading('stop');
				if(data.code == 0){
					$('#h_cpn').val($('#cpn').val());
					$('#h_cpnp').val(data.cpnp);
					$('#cpnp').val(setComma(data.cpnp));

					var tot = 0;
					if($('#totcost').val() != "") {
						tot = $('#totcost').val();
					}
					tot = parseInt(tot) - parseInt(data.cpnp);

					$('#h_payment').val(tot);
					$('#payment').val(setComma(tot));

					//totcost
				}
				alert(data.message);
			},
			error : function() {
				$('body').loading('stop');
				alert("쿠폰 확인에 문제가 있습니다. 잠시후에 다시 이용하시기 바랍니다.");
			}
		});
	
	});
});

//이모지 문자 체크
function checkEmoji(value){
	var ranges = [
				  '\ud83c[\udf00-\udfff]', // U+1F300 to U+1F3FF
				  '\ud83d[\udc00-\ude4f]', // U+1F400 to U+1F64F
				  '\ud83d[\ude80-\udeff]'  // U+1F680 to U+1F6FF
				];
	if(value.match(new RegExp(ranges.join('|'), 'g')) == null) {
		return true;
	} else {
		return false;
	}
}

function checkTel(tel1, tel2, tel3){
	var tel = tel1 + tel2 + tel3;
	if(tel == "") return false;
	var regExpTel = /^0?1([0|1|6|7|8|9]?)-?([0-9]{3,4})-?([0-9]{4})$/;
	return regExpTel.test(tel);
}

function goOkpage(){
	var f = document.submitReqForm;
	f.target = '_self';
	f.method = 'post';
	f.enctype = "application/x-www-form-urlencoded";
	if($('#h_stype').val() == '1') {
		f.action = './p_test_req_ok.html';
	} else {
		f.action = './p_move_req_ok.html';
	}
	f.submit();
}

//숫자에 화폐단위 콤마찍기
function numberWithCommas(x) {
    return x.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");
}