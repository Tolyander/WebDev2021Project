export interface Product {
    id: number;
    name: string;
    category: string;
    price: number;
    rating: string;
    description: string;
    image: string;
    url: string;
}

export interface Category {
    category: string;
}

export interface Phone {
    title: string;
    price: number;
    company: string;
}

export interface AuthToken {
    token: string;
}