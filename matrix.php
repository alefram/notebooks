<?php

// A node class 
class Node 
{ 
	public $data; 
	public $next; 
	
	function __construct($data) 
	{ 
		$this->data = $data; 
		$this->next = NULL; 
	} 
} 

// Linked List class 
class LinkedList 
{ 
	// Head of list 
	public $head; 

	// Function to insert a new node 
	public function insert($data) 
	{ 
		// Create a new node 
		$node = new Node($data); 
		
		// If list is empty make it head 
		if (empty($this->head)) { 
			$this->head = $node; 
		} 
		else { 
			$current = $this->head; 

			// Find the last node 
			while ($current->next != NULL) { 
				$current = $current->next; 
			} 

			// Append new node at the end 
			// of the list 
			$current->next = $node; 
		} 
	} 

	// Function to print the list 
	public function display() 
	{ 
		$current = $this->head; 
		while ($current != NULL) { 
			echo $current->data . "\n"; 
			$current = $current->next; 
		} 
	} 
} 

// Create a list 
$list = new LinkedList(); 

// Insert some data 
$list->insert(1); 
$list->insert(2); 
$list->insert(3); 

// Print the list 
$list->display(); 
?>


