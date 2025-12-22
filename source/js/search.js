/**
 * Search functionality for Products and Projects
 * Allows bidirectional search: find products used in projects, and projects using specific products
 */

// Load data from JSON file
let productsData = [];
let projectsData = [];

// Load data when page loads
document.addEventListener('DOMContentLoaded', function() {
    loadData();
});

// Load JSON data
function loadData() {
    fetch('js/data.json')
        .then(response => response.json())
        .then(data => {
            productsData = data.products;
            projectsData = data.projects;
            initializeSearch();
        })
        .catch(error => {
            console.error('Error loading data:', error);
        });
}

// Initialize search functionality
function initializeSearch() {
    // Add search bar to projects page
    if (document.getElementById('projects-section')) {
        addSearchBarToProjects();
    }
    
    // Add search bar to products page
    if (document.getElementById('products-section')) {
        addSearchBarToProducts();
    }
}

// Add search bar to projects page
function addSearchBarToProjects() {
    const searchInput = document.getElementById('project-search-input');
    const searchBtn = document.getElementById('project-search-btn');
    
    if (searchInput && searchBtn) {
        searchBtn.addEventListener('click', searchProjects);
        searchInput.addEventListener('keypress', function(e) {
            if (e.key === 'Enter') {
                searchProjects();
            }
        });
    }
}

// Add search bar to products page
function addSearchBarToProducts() {
    const searchInput = document.getElementById('product-search-input');
    const searchBtn = document.getElementById('product-search-btn');
    
    if (searchInput && searchBtn) {
        searchBtn.addEventListener('click', searchProducts);
        searchInput.addEventListener('keypress', function(e) {
            if (e.key === 'Enter') {
                searchProducts();
            }
        });
    }
}

// Search projects and filter the project list
function searchProjects() {
    const searchTerm = document.getElementById('project-search-input').value.toLowerCase().trim();
    const resultsDiv = document.getElementById('search-results');
    const filtrContainer = document.querySelector('.filtr-container');
    
    if (!filtrContainer) return;
    
    // Clear previous search results message
    resultsDiv.innerHTML = '';
    
    if (!searchTerm) {
        // Show all projects
        const allItems = filtrContainer.querySelectorAll('.filtr-item');
        allItems.forEach(item => {
            item.style.display = '';
        });
        // Remove search-active class to restore full width
        filtrContainer.classList.remove('search-active');
        // Remove search-active-row class from parent row
        const parentRow = filtrContainer.closest('.row');
        if (parentRow) {
            parentRow.classList.remove('search-active-row');
        }
        // Hide products section
        const productsSection = document.getElementById('project-products-section');
        if (productsSection) {
            productsSection.innerHTML = '';
        }
        return;
    }
    
    // Find matching projects by name or description
    const matchingProjectsByName = projectsData.filter(project => 
        project.name.toLowerCase().includes(searchTerm) ||
        project.description.toLowerCase().includes(searchTerm)
    );
    
    // Find matching products
    const matchingProducts = productsData.filter(product =>
        product.name.toLowerCase().includes(searchTerm) ||
        product.description.toLowerCase().includes(searchTerm)
    );
    
    // Get project IDs to show
    let projectIdsToShow = new Set();
    
    // Add projects matched by name/description
    matchingProjectsByName.forEach(project => {
        projectIdsToShow.add(project.id);
    });
    
    // Add projects that use matching products
    matchingProducts.forEach(product => {
        projectsData.forEach(project => {
            if (project.products.includes(product.id)) {
                projectIdsToShow.add(project.id);
            }
        });
    });
    
    // Add search-active class to make container shrink
    filtrContainer.classList.add('search-active');
    // Add search-active-row class to parent row to make it shrink too
    const parentRow = filtrContainer.closest('.row');
    if (parentRow) {
        parentRow.classList.add('search-active-row');
    }
    
    // Filter and show/hide projects
    const allItems = filtrContainer.querySelectorAll('.filtr-item');
    let foundCount = 0;
    const foundProjects = [];
    
    allItems.forEach(item => {
        const projectId = item.getAttribute('data-project-id');
        if (projectId && projectIdsToShow.has(projectId)) {
            item.style.display = '';
            foundCount++;
            // Get project data
            const project = projectsData.find(p => p.id === projectId);
            if (project) {
                foundProjects.push(project);
            }
        } else {
            item.style.display = 'none';
        }
    });
    
    // Show message if no results
    if (foundCount === 0) {
        resultsDiv.innerHTML = '<div class="alert alert-info mt-3">Không tìm thấy dự án nào.</div>';
        // Hide products section
        const productsSection = document.getElementById('project-products-section');
        if (productsSection) {
            productsSection.innerHTML = '';
        }
    } else {
        // Display products used in found projects
        displayProjectProducts(foundProjects);
    }
}

// Display products used in projects
function displayProjectProducts(projects) {
    const productsSection = document.getElementById('project-products-section');
    if (!productsSection) return;
    
    if (projects.length === 0) {
        productsSection.innerHTML = '';
        return;
    }
    
    // Collect all unique products from all projects
    const allProductIds = new Set();
    projects.forEach(project => {
        project.products.forEach(productId => {
            allProductIds.add(productId);
        });
    });
    
    // Get product details
    const productsToShow = Array.from(allProductIds).map(productId => {
        return productsData.find(p => p.id === productId);
    }).filter(p => p !== undefined);
    
    if (productsToShow.length === 0) {
        productsSection.innerHTML = '';
        return;
    }
    
    // Build HTML for products
    let html = `
        <div class="col-12">
            <div class="title text-center mb-4" style="margin-top: 20px;">
                <h3>Sản Phẩm Đã Sử Dụng</h3>
                <p>Các sản phẩm kính được sử dụng trong ${projects.length} dự án tìm được</p>
                <div class="border"></div>
            </div>
        </div>
    `;
    
    productsToShow.forEach(product => {
        html += `
            <div class="col-lg-4 col-md-6 mb-4">
                <div class="product-item text-center">
                    <div class="product-image mb-3">
                        <img loading="lazy" src="${product.image}" class="img-fluid" alt="${product.name}">
                    </div>
                    <h4><a href="${product.link}">${product.name}</a></h4>
                    <p>${product.description.substring(0, 150)}...</p>
                    <a href="${product.link}" class="btn btn-main">Xem Chi Tiết</a>
                </div>
            </div>
        `;
    });
    
    productsSection.innerHTML = html;
}

// Search products and filter projects on products page
function searchProducts() {
    const searchTerm = document.getElementById('product-search-input').value.toLowerCase().trim();
    const resultsDiv = document.getElementById('product-search-results');
    
    // Clear previous search results message
    resultsDiv.innerHTML = '';
    
    if (!searchTerm) {
        return;
    }
    
    // Find matching products
    const matchingProducts = productsData.filter(product =>
        product.name.toLowerCase().includes(searchTerm) ||
        product.description.toLowerCase().includes(searchTerm)
    );
    
    // Find matching projects by name or description
    const matchingProjectsByName = projectsData.filter(project => 
        project.name.toLowerCase().includes(searchTerm) ||
        project.description.toLowerCase().includes(searchTerm)
    );
    
    // Get project IDs that use matching products
    let projectIdsToShow = new Set();
    
    // Add projects matched by name/description
    matchingProjectsByName.forEach(project => {
        projectIdsToShow.add(project.id);
    });
    
    // Add projects that use matching products
    matchingProducts.forEach(product => {
        projectsData.forEach(project => {
            if (project.products.includes(product.id)) {
                projectIdsToShow.add(project.id);
            }
        });
    });
    
    // If we're on projects page, filter the projects
    const filtrContainer = document.querySelector('.filtr-container');
    if (filtrContainer) {
        // Add search-active class to make container shrink
        filtrContainer.classList.add('search-active');
        // Add search-active-row class to parent row to make it shrink too
        const parentRow = filtrContainer.closest('.row');
        if (parentRow) {
            parentRow.classList.add('search-active-row');
        }
        
        const allItems = filtrContainer.querySelectorAll('.filtr-item');
        let foundCount = 0;
        
        allItems.forEach(item => {
            const projectId = item.getAttribute('data-project-id');
            if (projectId && projectIdsToShow.has(projectId)) {
                item.style.display = '';
                foundCount++;
            } else {
                item.style.display = 'none';
            }
        });
        
        // Show message if no results
        if (foundCount === 0) {
            resultsDiv.innerHTML = '<div class="alert alert-info mt-3">Không tìm thấy dự án nào.</div>';
        }
    } else {
        // If not on projects page, show message
        if (projectIdsToShow.size === 0) {
            resultsDiv.innerHTML = '<div class="alert alert-info mt-3">Không tìm thấy dự án nào sử dụng sản phẩm này.</div>';
        } else {
            resultsDiv.innerHTML = `<div class="alert alert-success mt-3">Tìm thấy ${projectIdsToShow.size} dự án. Vui lòng vào trang Dự Án để xem chi tiết.</div>`;
        }
    }
}

