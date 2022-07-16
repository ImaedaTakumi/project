/*https://coco-factory.jp/ugokuweb/move01/5-1-5/から引用*/
//スクロールすると上部に固定させるための設定を関数でまとめる
function FixedAnime() {
    var headerH = $('#header').outerHeight(true);
    var scroll = $(window).scrollTop();
    if (scroll >= headerH){//headerの高さ以上になったら
            $('#header').addClass('fixed');//fixedというクラス名を付与
        }else{//それ以外は
            $('#header').removeClass('fixed');//fixedというクラス名を除去
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
$(function(){
    $(window).on('load scroll',function (){
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
                    $('.animation_before').addClass('active')
                }, 500)
            }
        });
    });
});
