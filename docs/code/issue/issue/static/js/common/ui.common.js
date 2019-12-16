StrUtil = window.StrUtil || {
	toInt:function(num){
		if(num == undefined || num == null || num == '' || num == 'NaN'){
			num = '0';
		}
		return parseInt(num);
	},
	cutString:function(str,len){
		var len  = len | 10;
		if(str != null && str != ''){
			if(str.length > len){
				str = str.substring(0,len) + '...';
			}
		}
		return str;
	},
	subStr:function(str, len){
	    if(!str) { return ''; }
	        len = len > 0 ? len*2 : 280;
	    var count = 0,	//计数：中文2字节，英文1字节
	        temp = '';  //临时字符串
	    for (var i = 0;i < str.length;i ++) {
	    	if (str.charCodeAt(i) > 255) {
	        	count += 2;
	        } else {
	        	count ++;
	        }
	        //如果增加计数后长度大于限定长度，就直接返回临时字符串
	        if(count > len) { return temp; }
	        //将当前内容加到临时字符串
	         temp += str.charAt(i);
	    }
	    return str;
	},
	//字符串长度-中文和全角符号为1，英文、数字和半角为0.5
	getLength:function(str, shortUrl) {
		if (true == shortUrl) {
			return Math.ceil(str.replace(/((news|telnet|nttp|file|http|ftp|https):\/\/){1}(([-A-Za-z0-9]+(\.[-A-Za-z0-9]+)*(\.[-A-Za-z]{2,5}))|([0-9]{1,3}(\.[0-9]{1,3}){3}))(:[0-9]*)?(\/[-A-Za-z0-9_\$\.\+\!\*\(\),;:@&=\?\/~\#\%]*)*/ig, 'http://goo.gl/fkKB ')
								.replace(/^\s+|\s+$/ig,'').replace(/[^\x00-\xff]/ig,'xx').length/2);
		} else {
			return Math.ceil(str.replace(/^\s+|\s+$/ig,'').replace(/[^\x00-\xff]/ig,'xx').length/2);
		}
	},
	getUUID:function() {
	    var d = new Date().getTime();
	    var uuid = 'xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx'.replace(/[xy]/g, function(c) {
	        var r = (d + Math.random()*16)%16 | 0;
	        d = Math.floor(d/16);
	        return (c=='x' ? r : (r&0x7|0x8)).toString(16);
	    });
	    return uuid;
	},
	fixNull:function(str){
		return str || '';
	}
}


/**
 * 网络操作
 */
Net = window.Net || {
	get:function(options){
		var defaults = {
			type: 'GET',
		};
		var opts = $.extend(defaults, options);
		this.ajax(opts);
	},
	post:function(options){
		var defaults = {
				type: 'POST',
		};
		var opts = $.extend(defaults, options);
		this.ajax(opts);
	},
	ajax:function(options){
		var opts = {};
		var defaults = {
		   //private params
		   reload:false,
		   go:null,
		   boxClose:false,
		   btn:null,
		   icon:$("#iconWait"),
		   callback:null,

		   //Jquery params
		   type: "GET",
		   dataType:"json",   //期待服务器返回的数据类型

		   cache: false,
		   url: null,
		   beforeSend:function(){  //ajax发送之前
			   if(opts.btn != null){
				   opts.btn.attr('disabled','disabled');
			   }
			   if(opts.icon != null){
				   opts.icon.addClass("fa fa-spinner fa-spin")
			   }
		   },
		   complete:function(){   //ajax请求结束
			   if(opts.btn != null){
				   opts.btn.attr('disabled',null);
			   }
			   if(opts.icon != null){
				  opts.icon.removeClass("fa fa-spinner fa-spin")
			   }
           },
		   success: function(resp, textStatus, jqXHR){  //ajax请求成功
			   switch (resp.status) {
				   case 0: // if resp.status==0
		            ui.msg.success( resp.msg ); //显示信息
		            if(opts.callback != null && $.isFunction(opts.callback)){
		                opts.callback(resp);
		            }
		            if(opts.reload){
		            	ui.reload();
		            }
		            if(opts.go != null && opts.go != ''){
		            	ui.go( opts.go );
		            }
		            if(opts.boxClose){
		            	ui.boxClose();
		            }
					if(opts.icon != null){
	 				   opts.icon.removeClass("fa fa-spinner fa-spin")
	 			   	}
		            break;
		        case 1:
		            ui.msg.fail( resp.msg );
					if(opts.icon != null){
	 				   opts.icon.removeClass("fa fa-spinner fa-spin")
	 			   	}
		            if(opts.callback != null && $.isFunction(opts.callback)){
		                opts.callback(resp);
		            }
		            break;
		        case -1:
		        	ui.msg.error( resp.msg );
					if(opts.icon != null){
	 				   opts.icon.removeClass("fa fa-spinner fa-spin")
	 			   	}
		            if(opts.callback != null && $.isFunction(opts.callback)){
		                opts.callback(resp);
		            }
					break
		      }
		   },
          statusCode: {
            403: function() {
               ui.msg.warning("没有权限!");
            }
          },
		   error:function(xhr){   //请求失败
               if (xhr.status==404){
			       ui.msg.warning("该记录不存在或被删除!");
               }else if(xhr.status == 403){
			       ui.msg.warning("没有权限!");
               }else if(xhr.status == 500){
			       ui.msg.warning("系统错误!");
               }else{
			       ui.msg.warning( ui.msg.CONST.MSG_BAD_REQUEST );
               }
			   if(opts.icon != null){
				  opts.icon.removeClass("fa fa-spinner fa-spin")
			   }
		   }
		};

		opts = $.extend(defaults, options);
		$.ajax( opts );
	},
	ajaxForm:function(options){
		var opts = {};
		var defaults = {
			form: $('#inputForm'),
			btn: $('#sbmBtn'),
			checkForm:true,
			boxClose:false,
			go:null,
	        dataType:"json",
	        beforeSerialize:function(){
	        	return true;
	        },
	        beforeSubmit: function(){
	           if( opts.btn != null ){
	        	   opts.btn.attr("disabled","disabled").addClass("disabled");
	           }
		       return true;
	        },
	        clearForm: false,
	        resetForm: false,
	        success: function(resp){
	        	switch (resp.status) {
				    case 0:
			            ui.msg.success(resp.msg);
			            if(opts.go != null ){
			            	ui.go(opts.go);
			            }
			            break;
			        case 1:
			            ui.msg.fail(resp.msg);
			            break;
			        case -1:
			        	ui.msg.error(resp.msg);
		      }
	          if( opts.btn != null ){
	        	  opts.btn.attr("disabled",null).removeClass("disabled");
		      }
	          if(opts.boxClose){
	        	  ui.boxClose();
	          }
	        },
	        error:function(resp){
	        	ui.msg.warning( ui.msg.CONST.MSG_BAD_REQUEST );

	        	if( opts.btn != null ){
	        		opts.btn.attr("disabled",null).removeClass("disabled");
			    }
	        }
		};
		opts = $.extend(defaults, options);

		if(opts.form == null){
			ui.msg.warning( 'FORM NOT FOUND');
			return;
		}
		if(opts.btn == null){
			ui.msg.warning( 'SUBMIT BUTTON NOT FOUND');
			return;
		}

		if(opts.checkForm){
			opts.form.checkForm();
		}
		opts.form.ajaxForm(opts);
	}
};

/*
 * 功能：页面通用的UI操作
 */
ui = window.ui ||{
	go:function(url,timeout){
		if(url != null && url != ''){
			timeout = timeout || 1000;
			setTimeout(function(){
				document.location.href = url; //跳转
			},timeout);
		}
	},
	to:function(url){
		document.location.href = url;
	},
	reload:function(){
		setTimeout(function(){
			document.location.reload(); //重新加载
		},1000);
	},
	confirm:function(msg,myCallBack,appendHtml){
		var content = '<div class="alert alert-warning text-center"><i class="glyphicon glyphicon-warning-sign fa fa-warning bigger-120"></i> <strong>'+msg+'</strong></div>';
		if(appendHtml!=null&&appendHtml!=''){
			content = content + appendHtml;
		}
		var uibox = $.scojs_confirm({
			  content: content, //确认框内容
			  action: myCallBack  //确认后要做的事
		});
		uibox.show();

		//see sco.confirm.js --> id="uiBoxCancellBtn"
		$('#uiBoxCancellBtn').click(function(){
			uibox.destroy();
		});
		$('#uiBoxYeapBtn').click(function(){
			uibox.destroy();
		});
	},
	msg:{
		CONST:{
			MSG_SUCCESS:"操作成功",
			MSG_FAIL:"操作失败",
			MSG_INFO:"操作信息",
			MSG_WARNING:"操作警告",
			MSG_ERROR:"系统错误",
			MSG_BAD_REQUEST:"请求发送失败"
		},
		success:function(msg,callback){
			this._showMsg({
				level:'SUCCESS',
				msg:msg,
				callback:callback
			});
		},
		fail:function(msg,callback){
			this._showMsg({
				level:'FAIL',
				msg:msg,
				callback:callback
			});
		},
		info:function(msg,callback){
			this._showMsg({
				level:'INFO',
				msg:msg,
				callback:callback
			});
		},
		warning:function(msg,callback){
			this._showMsg({
				level:'WARNING',
				msg:msg,
				callback:callback
			});
		},
		error:function(msg,callback){
			this._showMsg({
				level:'ERROR',
				msg:msg,
				callback:callback
			});
		},
		_showMsg:function(options){
			var opts = {
				msg:null,
				level:'ERROR',
				callback:null
			}
			opts = $.extend(opts, options);
			//fixed if the first param is function
			if(opts.msg != null && $.isFunction(opts.msg) ){
				opts.callback = opts.msg;
				opts.msg = null;
			}

			var _self = this;
			var msgTxt = '';

			switch (opts.level) {
				case 'SUCCESS':
					msgTxt = '<div><i class="glyphicon glyphicon-ok-circle fa-ok-circle"></i> '+ (opts.msg || _self.CONST.MSG_SUCCESS) +'</div>';
					$.scojs_message(msgTxt,$.scojs_message.TYPE_OK);
					//smoke.signal(msg,2300);
					break;
				case 'FAIL':
					msgTxt = '<div><i class="glyphicon glyphicon-remove-circle fa-remove-circle"></i> '+ (opts.msg  || _self.CONST.MSG_FAIL)  +'</div>';
					$.scojs_message(msgTxt,$.scojs_message.TYPE_ERROR);
					break;
				case 'INFO':
					msgTxt = '<div><i class="glyphicon glyphicon-exclamation-sign  fa-exclamation-sign"></i> '+ (opts.msg || _self.CONST.MSG_INFO) +'</div>';
					$.scojs_message(msgTxt,$.scojs_message.TYPE_INFO);
					break;
				case 'WARNING':
					msgTxt = '<div><i class="glyphicon glyphicon-warning-sign  fa fa-warning"></i> '+ (opts.msg  || _self.CONST.MSG_WARNING)  +'</div>';
					$.scojs_message(msgTxt,$.scojs_message.TYPE_WARNING);
					break;
				default://FAIL
					msgTxt = '<div><i class="glyphicon glyphicon-remove-circle fa-remove-circle"></i> '+ (opts.msg  || _self.CONST.MSG_ERROR)  +'</div>';
					$.scojs_message(msgTxt,$.scojs_message.TYPE_ERROR);
					break;
			}
			if(opts.callback != null && $.isFunction(opts.callback)){
				opts.callback();
			}
		}
	},
	box:function(options){
		var defaults = {
			title:'网页信息',
			content:'',
			size: 'lg',
			backdrop:true,
			keyboard:true,
			show:true,
			footer:false,
			remote:false,
			method:'GET',
			param:{},
			btn:''
		};
		var opts = $.extend(defaults, options);
		var jBoxWidth = 650;
		var jBoxHeight = 450;

		if(opts.size != ''){
			var sizeClass = '';
			if(opts.size == 'sm' ){
				var jBoxWidth = 500;
				var jBoxHeight = 350;
			}
			if(opts.size == 'mid' ){
				var jBoxWidth = $(window).width() - 400;
				var jBoxHeight = 200;
			}
			if(opts.size == 'lg' ) {
				var jBoxWidth =  $(window).width() - 300;
				var jBoxHeight = 'auto';
			}
			if(opts.size == 'xlg' ) {
				var jBoxWidth =  $(window).width() - 50;
				var jBoxHeight = 'auto';
			}
			$('#myUIBoxWrapper').addClass( sizeClass );
		};

		var ajaxOptions = null;
		if(opts.remote != ''){
			ajaxOptions = {
				type:opts.method,
				dataType:"html",
				cache: false,
				url: opts.remote,
				data: opts.param,
			    reload: false,
			    setContent: true,
			    spinner: true,
                error:function(xhr){
                   if (xhr.status==404){
                       ui.msg.warning("该记录不存在或被删除!");
                   }
                },
                statusCode: {
                  403: function() {
                   ui.msg.warning("没有权限!");
                   //this.close();
                   return
                }
          },

			}
			opts.remote = false;
		}

		return new jBox('Modal', {
			trigger:'click',//定义关闭的类型，click,mouseenter,touchclick
		    width: jBoxWidth,
		    height: jBoxHeight,
		    minWidth: 500,
		    minHeight: 350,
		    maxHeight: $(window).width() - 200,
		    maxHeight: $(window).height() - 150,
		    //animation:{open: 'tada', close: 'flip'},
		    //animation:{open: 'zoomIn', close: 'tada'},
		    overlay:true, //是否要遮盖原来页面
		    closeOnClick: false,
		    appendTo:$('body'), //绑定位置
			draggable:false, //设置拖动
		    attach: $('#myModal'),
		    title: opts.title,
		    ajax:ajaxOptions,
		    content: opts.content,
		    closeButton:'box',
			animation: 'flip', //设置滑出动画
		    onCreated: function() {
		    	if(opts.footer){
		    		this.footer = jQuery('<div class="jBox-Confirm-footer" style="text-align:right;"/>');
					jQuery('<span>'+opts.btn+'&nbsp;</span>').appendTo(this.footer);
					jQuery('<span style="margin:0 12px;"><a href="javascript:void(0)" class="btn btn-sm btn-danger">&nbsp;'+this.options.cancelButton+'&nbsp;</a></span>').click(function() {this.options.cancel && this.options.cancel(); this.close();}.bind(this)).appendTo(this.footer);
					this.footer.appendTo(this.container);
		    	}
			},
			onCloseComplete: function() {
				this.destroy();
			}
		}).open();
	},
	boxClose:function(){
		$('.jBox-closeButton').click(); //关闭
	}
};
var checkAll = {
  isChecked:function(){
	  var $chkarry = $('input:checked').not($('#checkedAll'));
	  if( $chkarry != null && $chkarry.length > 0){
		  return true;
	  }else{
		  return false;
	  }
  },
  isCheckedOne:function(){
	  var $chkarry = $('input:checked').not($('#checkedAll'));
	  if( $chkarry != null && $chkarry.length == 1){
		  return true;
	  }else{
		  ui.msg.warning('请勾选一条需要操作的数据！');
		  return false;
	  }
  },
  getId:function(){
	  return $('input:checked').not($('#checkedAll'))[0].value;
  },
  getIdsAsArr:function(){
	  var $chkarry = $('input:checked').not($('#checkedAll'));
	  var params = new Array();
	  for(var i=0;i<$chkarry.length;i++){
		  params.push( $chkarry[i].value );
	  }
	  return params;
  },
  getIdsAsStr:function(){
	  var $chkarry = $('input:checked').not($('#checkedAll'));
	  var params = '';
	  for(var i=0;i<$chkarry.length;i++){
		  params += $chkarry[i].value + ",";
	  }
	  params = params.substring(0,params.length - 1);
	  return params;
  },
  highlight:function(){
	  $(".ace").not($('#checkedAll')).on('change',function(){
		  var obj = $(this);
		  var status = obj.attr('checkStatus');
		  if(status == null){
			  obj.parent().parent().parent().addClass("warning");
			  obj.attr('checkStatus',1);
		  }else{
			  obj.parent().parent().parent().removeClass("warning");
			  obj.attr('checkStatus',null);
		  }
	  })
  }
}

/**
 * checkAll 操作
 */
$(function() {
	$('table th input:checkbox').on('click' , function(){
		var that = this;
		$(this).closest('table').find('tr > td:first-child input:checkbox')
		.each(function(){
			this.checked = that.checked;
			$(this).closest('tr').toggleClass('selected');
		});
	});

	checkAll.highlight();
});
