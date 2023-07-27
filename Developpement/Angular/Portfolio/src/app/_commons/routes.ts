import { Routes } from '@angular/router';
import { ErrorComponent } from '../error/error.component';
import { AboutComponent } from '../main/about/about.component';
import { AllProductsComponent } from '../main/all-products/all-products.component';
import { ContactComponent } from '../main/contact/contact.component';
import { HomeComponent } from '../main/home/home.component';
import { MainComponent } from '../main/main.component';
import { OneProductComponent } from '../main/one-product/one-product.component';

export const ROUTES: Routes = [
  {
    path: '',
    component: MainComponent,
    children: [
      { path: '', component: HomeComponent },
      { path: 'contact', component: ContactComponent },
      { path: 'about', component: AboutComponent },
      { path: 'products', component: AllProductsComponent },
      { path: 'products/:id', component: OneProductComponent },
    ],
  },
  { path: '**', component: ErrorComponent },
];
