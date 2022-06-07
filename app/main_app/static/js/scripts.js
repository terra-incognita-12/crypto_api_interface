$(document).on('click', '.confirm-delete', function(){
    return confirm('Are you sure you want delete this?');
});

function getCurrencies() {
    const options = {method: 'GET', headers: {Accept: 'application/json'}};
    const currency_id_arr = [];

    fetch('https://api.exchange.coinbase.com/currencies', options)
        .then(response => response.json())
        .then(response => {
            for (let i = 0; i < response.length; i++) {
                currency_id_arr[i] = response[i]['id'];
            }
        })
        .catch(err => console.error(err));

    return currency_id_arr;
}

function getCurrencyBuyRate(buy_currency, sell_currency, buy_amount) {
    const options = {method: 'GET', headers: {Accept: 'application/json'}};
    fetch('https://api.coinbase.com/v2/prices/BTC-USD/buy', options)
        .then(response => response.json())
        .then(response => {
            var currency_rate = response['data']['amount'];
            // console.log(currency_rate);
            console.log(currency_rate);
            return currency_rate;
        })
        .catch(err => console.error(err));
        
    return;
}


$(function(){
    $('#tradeform_check_balance').click(function() {
        // currency_rate = getCurrencyBuyRate('BTC', 'USDT', 1);
        currency_rate = async () => {
            return 10;
        }
        // currency_rate = 10;
        alert(currency_rate);
        alert(1231);
    });
});

// $(function(){
//     $('body').on('input', '#tradeform_sell_currency', function(){
//         if($('#tradeform_buy_currency').val() && $('#tradeform_buy_amount').val() && $('#tradeform_sell_currency').val()) {
//             convertCurrency($('#tradeform_buy_currency').val(), $('#tradeform_sell_currency').val(), $('#tradeform_buy_amount').val());
//         }
//     });
// });

$(function(){
    const currency_arr = getCurrencies();
    $('.currency-autocomplete').autocomplete({
        source: currency_arr,
    });
});
