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
                currency_id_arr[i] = response[i]['id']
            }
        })
        .catch(err => console.error(err));

    return currency_id_arr;
}

// function convertCurrency(buy_currency, sell_currency, buy_amount) {
//     const data = { from: buy_currency, to: sell_currency, amount: buy_amount };
//     const options = {
//         method: 'POST',
//         headers: {Accept: 'application/json', 'Content-Type': 'application/json'},
//         body: JSON.stringify(data),
//     };
      
//     fetch('https://api.exchange.coinbase.com/conversions', options)
//         .then(response => response.json())
//         .then(response => console.log(response))
//         .catch(err => console.error(err));
// }

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
