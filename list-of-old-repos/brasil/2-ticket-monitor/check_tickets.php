<?php

$tickets = isset($_GET['id']) ? explode(',', $_GET['id']) : [];
$tickets = array_map(function($id) { return 'IMT' . $id; }, $tickets);

$ch = curl_init('https://fwctickets.fifa.com/TopsAkaCalls/Calls.aspx/getBasicData?l=en&c=BRA');
curl_setopt($ch, CURLOPT_USERAGENT, 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36');
curl_setopt($ch, CURLOPT_RETURNTRANSFER, TRUE);
$response = curl_exec($ch);
curl_close($ch);

$data = json_decode($response, true);
$data = json_decode($data['d']['data'], true);
$data = $data['BasicCodes']['PRODUCTPRICES'];

$availableTickets = [];

foreach ($data as $product) {
    if (in_array($product['PRPProductId'], $tickets) && $product['Quantity'] != '-1') {
        $availableTickets[] = $product['PRPProductId'];
    }
}

exit(json_encode(array_values(array_unique($availableTickets))));
