import { Link } from './models/link';
import { Product } from './models/product';

export const LINKS: Link[] = [
  { id: 0, path: '', name: 'Home', icon: '' },
  { id: 1, path: '/products', name: 'Products', icon: '' },
  { id: 2, path: '/about', name: 'A propos', icon: '' },
  { id: 3, path: '/contact', name: 'Contact', icon: '' },
];

export const PRODUCTS: Product[] = [
  {
    id: 748798,
    name: 'home',
    img: 'assets/product.png',
    description: 'deccription esteban',
    previews: [
      'https://ileauxepices.com/1354-product_zoom/graines-de-soja-grillees.jpg',
      'https://cdn.discordapp.com/attachments/483349134661779476/1029367018165633156/productpreview1.jpg',
      'assets/preview.png',
      'assets/productpreview1.png',
      'assets/productpreview1.png',
    ],
    path: '/product/533364',
  },
  {
    id: 2245,
    name: 'contact',
    description: 'deccription kwency',
    img: 'assets/product.png',
    previews: [
      'https://ileauxepices.com/1354-product_zoom/graines-de-soja-grillees.jpg',
      'https://cdn.discordapp.com/attachments/483349134661779476/1029367018165633156/productpreview1.jpg',

      'assets/preview.png',
      'assets/productpreview1.png',
      'assets/productpreview1.png',
    ],
    path: '/product/234',
  },
];
