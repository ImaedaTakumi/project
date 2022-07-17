/*https://coco-factory.jp/ugokuweb/move01/5-1-5/から引用*/
//スクロールすると上部に固定させるための設定を関数でまとめる
function FixedAnime() {
    var headerH = 1000;
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

/*スクロール*/
function ScrollWindow(elem) {
    var element = document.getElementById(elem);
    var rect = element.getBoundingClientRect();
    var elemtop = rect.top + window.pageYOffset;
    document.documentElement.scrollTop = elemtop;
}

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
        }
    });
}

$(window).on('load',function (){//ページがロードされたら
    animation()//アニメーション実行
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
});