export interface Product {
    id: number;
    name: string;
    color: string;
    Os: string;
    hasNfc: boolean;
    ram: number;
    rom: number;
    camera: string;
    category: number;
    price: number;
    likes: number;
    link: string;
    imageUrl: string;
}

export const products = [
    {
        id: 1,
        name: 'Google Pixel 7',
        color: 'black',
        Os: 'Android 13',
        hasNfc: true,
        ram: 8,
        rom: 128,
        camera: '50MP + 12MP',
        category: 1,
        price: 217001,
        likes: 0,
        link: 'https://kaspi.kz/shop/p/google-pixel-7-8-gb-128-gb-chernyi-106971937/?c=750000000',
        imageUrl: 'https://resources.cdn-kaspi.kz/img/m/p/hfe/hb5/84424699838494.png?format=gallery-medium'
    },
    {
        id: 2,
        name: 'Xiaomi Redmi Note 12 Pro',
        color: 'gray',
        Os: 'Android 12',
        hasNfc: true,
        ram: 8,
        rom: 256,
        camera: '108MP + 8MP + 2MP + 5MP',
        category: 2,
        price: 121885,
        likes: 0,
        link: 'https://kaspi.kz/shop/p/google-pixel-7-8-gb-128-gb-chernyi-106971937/?c=750000000',
        imageUrl: 'https://resources.cdn-kaspi.kz/img/m/p/h02/ha0/79846423199774.jpg?format=gallery-medium'
    },
    {
        id: 3,
        name: 'IPhone 15 Pro Max',
        color: 'black',
        Os: 'iOS 17',
        hasNfc: true,
        ram: 8,
        rom: 1024,
        camera: '48MP + 12MP + 12MP',
        category: 3,
        price: 940894,
        likes: 0,
        link: 'https://kaspi.kz/shop/p/google-pixel-7-8-gb-128-gb-chernyi-106971937/?c=750000000',
        imageUrl: 'https://resources.cdn-kaspi.kz/img/m/p/hc6/h5d/84076355977246.jpg?format=gallery-medium'
    },
    {
        id: 4,
        name: 'OPPO Reno 8T',
        color: 'black',
        Os: 'Android 13',
        hasNfc: true,
        ram: 8,
        rom: 128,
        camera: '100MP + 2MP + 2MP',
        category: 4,
        price: 139500,
        likes: 0,
        link: 'https://kaspi.kz/shop/p/google-pixel-7-8-gb-128-gb-chernyi-106971937/?c=750000000',
        imageUrl: 'https://resources.cdn-kaspi.kz/img/m/p/h4e/h64/70342818955294.jpg?format=gallery-medium'
    },
    {
        id: 5,
        name: 'OPPO Reno 8T',
        color: 'black',
        Os: 'Android 13',
        hasNfc: true,
        ram: 8,
        rom: 128,
        camera: '100MP + 2MP + 2MP',
        category: 4,
        price: 139500,
        likes: 0,
        link: 'https://kaspi.kz/shop/p/google-pixel-7-8-gb-128-gb-chernyi-106971937/?c=750000000',
        imageUrl: 'https://resources.cdn-kaspi.kz/img/m/p/h4e/h64/70342818955294.jpg?format=gallery-medium'
    },
    {
        id: 6,
        name: 'Google Pixel 8',
        color: 'black',
        Os: 'Android',
        hasNfc: true,
        ram: 8,
        rom: 128,
        camera: '50MP + 12MP',
        category: 1,
        price: 285900,
        likes: 0,
        link: 'https://kaspi.kz/shop/p/google-pixel-8-8-gb-128-gb-chernyi-113692654/?c=750000000',
        imageUrl: 'https://resources.cdn-kaspi.kz/img/m/p/hcf/he9/84136091254814.jpg?format=gallery-medium'
    },
    {
        id: 7,
        name: 'Google Pixel 7 Pro',
        color: 'black',
        Os: 'Android 13',
        hasNfc: true,
        ram: 12,
        rom: 128,
        camera: '50MP + 12MP + 48MP',
        category: 1,
        price: 274899,
        likes: 0,
        link: 'https://kaspi.kz/shop/p/google-pixel-7-pro-12-gb-128-gb-chernyi-107066141/?c=750000000',
        imageUrl: 'https://resources.cdn-kaspi.kz/img/m/p/h26/h67/63603038289950.jpg?format=gallery-medium'
    },
    {
        id: 8,
        name: 'Google Pixel 7A',
        color: 'black',
        Os: 'Android 13',
        hasNfc: true,
        ram: 8,
        rom: 128,
        camera: '100MP + 2MP + 2MP',
        category: 1,
        price: 139500,
        likes: 0,
        link: 'https://kaspi.kz/shop/p/google-pixel-7a-8-gb-128-gb-chernyi-110489765/?c=750000000',
        imageUrl: 'https://resources.cdn-kaspi.kz/img/m/p/hcd/h87/80879192047646.jpg?format=gallery-medium'
    },
    {
        id: 9,
        name: 'Google Pixel 8 Pro',
        color: 'beige',
        Os: 'Android',
        hasNfc: true,
        ram: 12,
        rom: 128,
        camera: '50MP + 48MP + 48MP',
        category: 1,
        price: 139500,
        likes: 0,
        link: 'https://kaspi.kz/shop/p/google-pixel-8-pro-12-gb-128-gb-bezhevyi-113692579/?c=750000000',
        imageUrl: 'https://resources.cdn-kaspi.kz/img/m/p/hfe/h21/84136159182878.jpg?format=gallery-medium'
    },
    {
        id: 10,
        name: 'OPPO Reno 8T',
        color: 'black',
        Os: 'Android 13',
        hasNfc: true,
        ram: 8,
        rom: 128,
        camera: '100MP + 2MP + 2MP',
        category: 2,
        price: 139500,
        likes: 0,
        link: 'https://kaspi.kz/shop/p/google-pixel-7-8-gb-128-gb-chernyi-106971937/?c=750000000',
        imageUrl: 'https://resources.cdn-kaspi.kz/img/m/p/h4e/h64/70342818955294.jpg?format=gallery-medium'
    },
    {
        id: 11,
        name: 'OPPO Reno 8T',
        color: 'black',
        Os: 'Android 13',
        hasNfc: true,
        ram: 8,
        rom: 128,
        camera: '100MP + 2MP + 2MP',
        category: 2,
        price: 139500,
        likes: 0,
        link: 'https://kaspi.kz/shop/p/google-pixel-7-8-gb-128-gb-chernyi-106971937/?c=750000000',
        imageUrl: 'https://resources.cdn-kaspi.kz/img/m/p/h4e/h64/70342818955294.jpg?format=gallery-medium'
    },
    {
        id: 12,
        name: 'OPPO Reno 8T',
        color: 'black',
        Os: 'Android 13',
        hasNfc: true,
        ram: 8,
        rom: 128,
        camera: '100MP + 2MP + 2MP',
        category: 2,
        price: 139500,
        likes: 0,
        link: 'https://kaspi.kz/shop/p/google-pixel-7-8-gb-128-gb-chernyi-106971937/?c=750000000',
        imageUrl: 'https://resources.cdn-kaspi.kz/img/m/p/h4e/h64/70342818955294.jpg?format=gallery-medium'
    },
    {
        id: 13,
        name: 'OPPO Reno 8T',
        color: 'black',
        Os: 'Android 13',
        hasNfc: true,
        ram: 8,
        rom: 128,
        camera: '100MP + 2MP + 2MP',
        category: 2,
        price: 139500,
        likes: 0,
        link: 'https://kaspi.kz/shop/p/google-pixel-7-8-gb-128-gb-chernyi-106971937/?c=750000000',
        imageUrl: 'https://resources.cdn-kaspi.kz/img/m/p/h4e/h64/70342818955294.jpg?format=gallery-medium'
    },
    {
        id: 14,
        name: 'OPPO Reno 8T',
        color: 'black',
        Os: 'Android 13',
        hasNfc: true,
        ram: 8,
        rom: 128,
        camera: '100MP + 2MP + 2MP',
        category: 3,
        price: 139500,
        likes: 0,
        link: 'https://kaspi.kz/shop/p/google-pixel-7-8-gb-128-gb-chernyi-106971937/?c=750000000',
        imageUrl: 'https://resources.cdn-kaspi.kz/img/m/p/h4e/h64/70342818955294.jpg?format=gallery-medium'
    },
    {
        id: 15,
        name: 'OPPO Reno 8T',
        color: 'black',
        Os: 'Android 13',
        hasNfc: true,
        ram: 8,
        rom: 128,
        camera: '100MP + 2MP + 2MP',
        category: 3,
        price: 139500,
        likes: 0,
        link: 'https://kaspi.kz/shop/p/google-pixel-7-8-gb-128-gb-chernyi-106971937/?c=750000000',
        imageUrl: 'https://resources.cdn-kaspi.kz/img/m/p/h4e/h64/70342818955294.jpg?format=gallery-medium'
    },
    {
        id: 16,
        name: 'OPPO Reno 8T',
        color: 'black',
        Os: 'Android 13',
        hasNfc: true,
        ram: 8,
        rom: 128,
        camera: '100MP + 2MP + 2MP',
        category: 3,
        price: 139500,
        likes: 0,
        link: 'https://kaspi.kz/shop/p/google-pixel-7-8-gb-128-gb-chernyi-106971937/?c=750000000',
        imageUrl: 'https://resources.cdn-kaspi.kz/img/m/p/h4e/h64/70342818955294.jpg?format=gallery-medium'
    },
    {
        id: 17,
        name: 'OPPO Reno 8T',
        color: 'black',
        Os: 'Android 13',
        hasNfc: true,
        ram: 8,
        rom: 128,
        camera: '100MP + 2MP + 2MP',
        category: 3,
        price: 139500,
        likes: 0,
        link: 'https://kaspi.kz/shop/p/google-pixel-7-8-gb-128-gb-chernyi-106971937/?c=750000000',
        imageUrl: 'https://resources.cdn-kaspi.kz/img/m/p/h4e/h64/70342818955294.jpg?format=gallery-medium'
    },
    {
        id: 18,
        name: 'OPPO Reno 8T',
        color: 'black',
        Os: 'Android 13',
        hasNfc: true,
        ram: 8,
        rom: 128,
        camera: '100MP + 2MP + 2MP',
        category: 4,
        price: 139500,
        likes: 0,
        link: 'https://kaspi.kz/shop/p/google-pixel-7-8-gb-128-gb-chernyi-106971937/?c=750000000',
        imageUrl: 'https://resources.cdn-kaspi.kz/img/m/p/h4e/h64/70342818955294.jpg?format=gallery-medium'
    },
    {
        id: 19,
        name: 'OPPO Reno 8T',
        color: 'black',
        Os: 'Android 13',
        hasNfc: true,
        ram: 8,
        rom: 128,
        camera: '100MP + 2MP + 2MP',
        category: 4,
        price: 139500,
        likes: 0,
        link: 'https://kaspi.kz/shop/p/google-pixel-7-8-gb-128-gb-chernyi-106971937/?c=750000000',
        imageUrl: 'https://resources.cdn-kaspi.kz/img/m/p/h4e/h64/70342818955294.jpg?format=gallery-medium'
    },
    {
        id: 20,
        name: 'OPPO Reno 8T',
        color: 'black',
        Os: 'Android 13',
        hasNfc: true,
        ram: 8,
        rom: 128,
        camera: '100MP + 2MP + 2MP',
        category: 4,
        price: 139500,
        likes: 0,
        link: 'https://kaspi.kz/shop/p/google-pixel-7-8-gb-128-gb-chernyi-106971937/?c=750000000',
        imageUrl: 'https://resources.cdn-kaspi.kz/img/m/p/h4e/h64/70342818955294.jpg?format=gallery-medium'
    }
];


/*
Copyright Google LLC. All Rights Reserved.
Use of this source code is governed by an MIT-style license that
can be found in the LICENSE file at https://angular.io/license
*/